# Technology Stack

## Frontend

- **React 18** with TypeScript for type-safe component development
- **Vite** as the build tool and dev server (fast HMR and optimized builds)
- **React Router DOM** for client-side routing in SPA
- **React Helmet Async** for SEO meta tag management
- **React Icons** for icon components

## Infrastructure & Deployment

- **AWS CDK (Python)** for Infrastructure as Code
- **AWS Solutions Constructs** for best-practice AWS patterns
- **CloudFront** for global CDN and HTTPS
- **S3** for static website hosting
- **Lambda** (via CDK deployment) for automated deployments

## Development Tools

- **TypeScript 5.4+** with strict mode enabled
- **ESLint** with TypeScript and React plugins
- **Sass** for advanced CSS features
- **esbuild** for fast bundling

## Common Commands

### Development
```bash
npm install          # Install dependencies
npm run dev          # Start dev server (http://localhost:5173)
npm run build        # Build for production (TypeScript check + Vite build)
npm run preview      # Preview production build locally
npm run lint         # Run ESLint checks
```

### Infrastructure (from /cdk directory)
```bash
# Setup
python3 -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
pip install -r requirements.txt

# CDK Commands
cdk bootstrap        # First-time setup (per account/region)
cdk synth           # Generate CloudFormation template
cdk deploy          # Deploy to AWS
cdk destroy         # Remove all AWS resources
cdk diff            # Show changes before deploy
```

### Full Deployment
```bash
npm run build       # Build frontend
cd cdk
cdk deploy         # Deploy infrastructure and content
```

## Build Configuration

- **Target**: ES2020 with modern browser support
- **Module System**: ESNext with bundler resolution
- **Asset Organization**: Separate directories for images, CSS, and JS
- **Output**: Optimized chunks with content hashing for cache busting
