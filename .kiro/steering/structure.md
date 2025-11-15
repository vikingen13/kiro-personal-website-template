# Project Structure

## Root Directory

```
/
├── src/              # React application source code
├── cdk/              # AWS CDK infrastructure code (Python)
├── public/           # Static assets served as-is
├── dist/             # Production build output (generated)
├── node_modules/     # Node dependencies (generated)
└── scripts/          # Build and automation scripts
```

## Source Code Organization (`/src`)

- **components/** - React components (pages, UI elements, shared components)
- **services/** - API integrations and external service clients
- **types/** - TypeScript type definitions and interfaces
- **data/** - Static data files (JSON, constants)
- **assets/** - Source assets that get processed by Vite
- **App.tsx** - Main application component with routing
- **main.tsx** - React application entry point
- **index.css** - Global styles
- **App.css** - Application-level styles

## Infrastructure (`/cdk`)

- **app.py** - CDK application entry point, defines stack and environment
- **personal_website_stack.py** - Main infrastructure stack definition
- **requirements.txt** - Python dependencies for CDK
- **cdk.json** - CDK configuration and context
- **test_config.py** - Infrastructure tests

## Static Assets (`/public`)

Files in this directory are served as-is without processing:
- **sitemap.xml** - SEO sitemap
- **robots.txt** - Search engine crawling rules
- **favicon.svg** - Site favicon
- **images/** - Static images

## Configuration Files

- **vite.config.ts** - Vite build configuration
- **tsconfig.json** - TypeScript compiler options for src/
- **tsconfig.node.json** - TypeScript config for Vite config files
- **.eslintrc.cjs** - ESLint rules and plugins
- **package.json** - Node dependencies and scripts

## Key Conventions

### Component Organization
- One component per file
- Component files use PascalCase (e.g., `ArticleCard.tsx`)
- Co-locate component-specific styles when needed

### TypeScript
- Strict mode enabled
- Explicit types preferred over inference for public APIs
- Interface definitions in `/types` directory for shared types

### Styling
- CSS modules or component-scoped styles
- Global styles in `index.css`
- Sass available for advanced features

### Infrastructure
- All AWS resources defined in CDK stack
- Use AWS Solutions Constructs for common patterns
- Tag all resources with "Project" tag
- Infrastructure code in Python, application code in TypeScript

### Build Output
- Production builds go to `/dist`
- Assets organized by type: `assets/images/`, `assets/css/`, `assets/js/`
- Content-hashed filenames for cache busting
