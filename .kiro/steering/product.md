# Product Overview

This is a personal website template designed for deployment on AWS infrastructure. The site serves as a professional portfolio and can be customized for various use cases including:

- Professional portfolios showcasing experience and projects
- Personal blogs with content integration
- Landing pages for freelance services
- Photo galleries with bio sections

The template is built for easy customization and automated deployment to AWS using Infrastructure as Code (CDK).

## Key Features

- Responsive, mobile-first design
- Single Page Application (SPA) with client-side routing
- Static site hosting on S3 with CloudFront distribution

## Target Audience

This template is designed for **non-developers** who want to create their own websites using AI-assisted coding. The infrastructure is pre-configured so users can focus on content and design.

## CRITICAL: Infrastructure Protection

**DO NOT modify any files in the `/cdk` directory unless explicitly requested by the user.**

The AWS CDK infrastructure is pre-configured and production-ready. Focus all customization efforts on:
- Website content and styling (`/src` directory)
- React components and pages
- Static assets (`/public` directory)
- Frontend configuration (Vite, TypeScript, ESLint)

Only modify CDK infrastructure files if the user specifically asks to change AWS deployment settings or infrastructure configuration.
