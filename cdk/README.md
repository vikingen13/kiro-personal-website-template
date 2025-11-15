# Infrastructure Documentation

This directory contains the AWS CDK infrastructure code that deploys your website to AWS.

## Architecture

Your website is deployed using a serverless architecture:

```
User → CloudFront (CDN) → S3 Bucket (Website Files)
```

### AWS Resources Created

1. **S3 Bucket** - Stores your website files (HTML, CSS, JS, images)
   - Private bucket (not publicly accessible)
   - Versioning enabled for rollback capability

2. **CloudFront Distribution** - Global CDN for fast content delivery
   - HTTPS enforced
   - Custom error pages for SPA routing (404/403 → index.html)
   - Global edge locations for low latency
   - Automatic cache invalidation on deployment

3. **Origin Access Control** - Secures S3 bucket
   - Only CloudFront can access the S3 bucket
   - No direct public access to files

4. **Lambda Function** - Automated deployment
   - Uploads website files to S3
   - Invalidates CloudFront cache
   - Triggered during CDK deployment

## Files

- **app.py** - CDK application entry point, defines the stack and AWS environment
- **personal_website_stack.py** - Main infrastructure definition using AWS Solutions Constructs
- **requirements.txt** - Python dependencies for CDK
- **cdk.json** - CDK configuration

## CDK Commands

```bash
# First-time setup
python3 -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt

# Bootstrap CDK (first time only, per account/region)
cdk bootstrap

# Preview changes
cdk synth          # Generate CloudFormation template
cdk diff           # Show what will change

# Deploy
cdk deploy         # Deploy infrastructure and website

# Clean up
cdk destroy        # Remove all AWS resources
```

## Configuration

### Region
Default region is `eu-west-1` (Ireland). To change:

Edit `app.py`:
```python
region=app.node.try_get_context("region") or "us-east-1"
```

Or pass via context:
```bash
cdk deploy -c region=us-east-1
```

### Tags
All resources are tagged with `Project: personal-website` for easy identification and cost tracking.

## Cost Optimization

The infrastructure uses:
- **AWS Solutions Constructs** - Pre-configured best practices
- **CloudFront Price Class 100** - North America and Europe only (cheapest)
- **No logging** - Reduces S3 storage costs
- **Lifecycle policies** - Automatic cleanup if logging is enabled

Typical monthly cost: **$1-5** (after AWS free tier)

## Security Features

- ✅ HTTPS only (TLS 1.2+)
- ✅ Private S3 bucket with Origin Access Control
- ✅ No public bucket access
- ✅ IAM least privilege via CDK
- ✅ Infrastructure as Code (auditable, reproducible)

## Troubleshooting

### Bootstrap Error
```bash
cdk bootstrap aws://ACCOUNT-ID/REGION
```

### Permission Denied
Ensure your AWS credentials have permissions for:
- CloudFormation
- S3
- CloudFront
- Lambda
- IAM (for creating roles)

### Deployment Stuck
Check CloudFormation console for detailed error messages.

### Cache Not Updating
Manually invalidate CloudFront cache:
```bash
aws cloudfront create-invalidation \
  --distribution-id YOUR_DIST_ID \
  --paths "/*"
```

## Customization

### Add Custom Domain

1. Request SSL certificate in AWS Certificate Manager (us-east-1 region)
2. Modify `personal_website_stack.py` to add certificate and domain
3. Update DNS records to point to CloudFront

### Enable Logging

Edit `personal_website_stack.py`:
```python
log_s3_access_logs=True,
log_cloud_front_access_log=True
```

### Change Cache Behavior

Modify CloudFront distribution props in `_create_cloudfront_s3_construct()`.

## Learn More

- [AWS CDK Documentation](https://docs.aws.amazon.com/cdk/)
- [AWS Solutions Constructs](https://docs.aws.amazon.com/solutions/latest/constructs/)
- [CloudFront Developer Guide](https://docs.aws.amazon.com/cloudfront/)
