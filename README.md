# 🚀 Personal Website Template

> **Create your own professional website in minutes with Kiro AI** - No coding required!

[![AWS](https://img.shields.io/badge/AWS-CloudFront%20%2B%20S3-orange)](https://aws.amazon.com)
[![React](https://img.shields.io/badge/React-18.x-blue)](https://reactjs.org)
[![Kiro](https://img.shields.io/badge/Powered%20by-Kiro%20AI-purple)](https://kiro.ai)

## What is this?

This template provides everything you need to create your own professional website using **Kiro AI**:

- 🏗️ **Pre-configured AWS infrastructure** (CDK code ready to deploy)
- 🎨 **Website template** (React + TypeScript starter)
- 🤖 **Kiro steering files** (guides Kiro to understand your project)

Just tell Kiro what you want, and it will customize the website for you. No coding knowledge needed!

Perfect for:
- 💼 Professional portfolios
- 📝 Personal blogs
- 🎨 Creative showcases
- 📧 Contact pages
- 🖼️ Photo galleries

## How it works

### 1. Tell Kiro what you want

Open Kiro and describe your website. For example:

```
"Create a portfolio website for me. I'm a photographer named Sarah Chen. 
Add an about section, a gallery of my work, and a contact page."
```

```
"Make this a personal blog about travel. Add a home page with recent posts 
and an about me section."
```

```
"Build a landing page for my freelance web design services. Include my 
services, portfolio, and contact form."
```

Kiro will customize the entire website for you!

### 2. Preview locally

```bash
npm install
npm run dev
```

Open http://localhost:5173 to see your site. Ask Kiro to make any changes you want.

### 3. Deploy to AWS

Once you're happy with your site, deploy it to the internet:

```bash
npm run build
cd cdk
cdk deploy
```

Your website will be live on AWS with a CloudFront URL!

## Prerequisites

Before you start, make sure you have:
- **Git** installed on your machine ([Download Git](https://git-scm.com/downloads))
- **Node.js 18+** installed ([Download Node.js](https://nodejs.org/))
- **Python 3.9+** installed ([Download Python](https://www.python.org/downloads/))

## First-time AWS setup

If this is your first time deploying:

```bash
# Install AWS CLI and configure your credentials
aws configure

# Set up CDK (one-time setup)
cd cdk
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
cdk bootstrap
```

## What you get

- ⚡ Fast, modern website built with React
- 🌐 Global CDN (CloudFront) for fast loading worldwide
- 🔒 Secure HTTPS hosting
- 📱 Mobile-friendly responsive design
- 💰 Low cost (~$1-5/month on AWS)

## Need help?

Just ask Kiro! Examples:

- "Change the color scheme to blue and white"
- "Add a new section about my skills"
- "Make the font bigger"
- "Add my social media links"
- "Create a contact form"

## Tech Stack

Built with React, TypeScript, Vite, and AWS CDK. But you don't need to know any of that - Kiro handles everything!

## Adding a custom domain

Want to use your own domain name (like `www.yourname.com`) instead of the CloudFront URL?

You can easily add a custom domain to your website! Follow this guide:

📖 [How to add a custom domain to CloudFront](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/CNAMEs.html)

**Quick overview:**
1. Register a domain (via Route 53 or any domain registrar)
2. Request an SSL certificate in AWS Certificate Manager
3. Add the domain to your CloudFront distribution
4. Update your DNS records to point to CloudFront

---

**Ready to build your website? Start by telling Kiro what you want!**
