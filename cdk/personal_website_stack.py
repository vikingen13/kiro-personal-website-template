from aws_cdk import (
    Stack,
    aws_s3_deployment as s3deploy,
    aws_cloudfront as cloudfront,
    aws_s3 as s3,
    RemovalPolicy,
    Duration,
    CfnOutput,
    Tags
)

from constructs import Construct
from aws_solutions_constructs.aws_cloudfront_s3 import CloudFrontToS3
import os

class PersonalWebsiteStack(Stack):
    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)
        
        # Tag toutes les ressources de la stack
        Tags.of(self).add("Project", "personal-website")
        
        # Create CloudFront + S3 using AWS Solutions Construct
        self.cloudfront_s3 = self._create_cloudfront_s3_construct()
        
        # Deploy website content
        self._deploy_website_content()
        
        # Create outputs
        self._create_outputs()
    
    def _create_cloudfront_s3_construct(self) -> CloudFrontToS3:
        """Create CloudFront + S3 using AWS Solutions Construct - Simple configuration"""
        
        # Simple CloudFront distribution props
        distribution_props = {
            "minimum_protocol_version": cloudfront.SecurityPolicyProtocol.TLS_V1_2_2021,
            "default_root_object": "index.html",
            "price_class": cloudfront.PriceClass.PRICE_CLASS_100,
            "comment": "CloudFront distribution for personal website - SPA routing enabled",
            "enabled": True,
	    "enable_logging": False
        }
        
        # Create the construct
        cloudfront_s3 = CloudFrontToS3(
            self, "CloudFrontS3",
            cloud_front_distribution_props=distribution_props,
            insert_http_security_headers=False,  # Disable to avoid CSP conflicts
            log_s3_access_logs=False,
            log_cloud_front_access_log=False
        )
        
        # Add SPA error responses manually to the distribution
        cfn_distribution = cloudfront_s3.cloud_front_web_distribution.node.default_child
        cfn_distribution.add_property_override("DistributionConfig.CustomErrorResponses", [
            {
                "ErrorCode": 403,
                "ResponseCode": 200,
                "ResponsePagePath": "/index.html",
                "ErrorCachingMinTTL": 0
            },
            {
                "ErrorCode": 404,
                "ResponseCode": 200,
                "ResponsePagePath": "/index.html",
                "ErrorCachingMinTTL": 0
            }
        ])
        
        # Add lifecycle policy to CloudFront logging bucket if it exists
        if cloudfront_s3.cloud_front_logging_bucket:
            cloudfront_s3.cloud_front_logging_bucket.add_lifecycle_rule(
                id="DeleteLogsAfter10Days",
                enabled=True,
                expiration=Duration.days(10),
                noncurrent_version_expiration=Duration.days(10)
            )
        
        return cloudfront_s3
    
    def _deploy_website_content(self):
        """Deploy website content to S3"""
        build_path = os.path.join(os.path.dirname(__file__), "..", "dist")
        
        if os.path.exists(build_path):
            s3deploy.BucketDeployment(
                self, "DeployWebsite",
                sources=[s3deploy.Source.asset(build_path)],
                destination_bucket=self.cloudfront_s3.s3_bucket_interface,
                distribution=self.cloudfront_s3.cloud_front_web_distribution,
                distribution_paths=["/*"],
                prune=True,
                retain_on_delete=False
            )
    
    def _create_outputs(self):
        """Create CloudFormation outputs"""
        
        # Website URL using CloudFront domain
        website_url = f"https://{self.cloudfront_s3.cloud_front_web_distribution.distribution_domain_name}"
        
        CfnOutput(
            self, "WebsiteURL",
            value=website_url,
            description="Website URL"
        )
        
        CfnOutput(
            self, "CloudFrontDistributionId",
            value=self.cloudfront_s3.cloud_front_web_distribution.distribution_id,
            description="CloudFront Distribution ID"
        )
        
        CfnOutput(
            self, "CloudFrontDomainName",
            value=self.cloudfront_s3.cloud_front_web_distribution.distribution_domain_name,
            description="CloudFront Domain Name"
        )
        
        CfnOutput(
            self, "S3BucketName",
            value=self.cloudfront_s3.s3_bucket_interface.bucket_name,
            description="S3 Bucket Name"
        )
