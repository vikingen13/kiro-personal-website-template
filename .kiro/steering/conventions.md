# Development Conventions

## Multi-Page Websites

When creating a website with multiple pages (Home, About, Contact, etc.):

### ✅ DO: Create separate page components

```
src/
├── components/
│   ├── Home.tsx        # Home page content
│   ├── About.tsx       # About page content
│   ├── Contact.tsx     # Contact page content
│   └── Blog.tsx        # Blog page content
└── App.tsx             # Routing and layout only
```

**Example App.tsx structure:**
```tsx
import { BrowserRouter, Routes, Route } from 'react-router-dom';
import Home from './components/Home';
import About from './components/About';
import Contact from './components/Contact';

function App() {
  return (
    <BrowserRouter>
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/about" element={<About />} />
        <Route path="/contact" element={<Contact />} />
      </Routes>
    </BrowserRouter>
  );
}
```

### ❌ DON'T: Put all content in App.tsx

Don't create a single massive App.tsx file with all page content. This makes the code hard to maintain and navigate.

## Component Best Practices

- **One responsibility per component** - Each component should do one thing well
- **Reusable components** - Extract common UI elements (buttons, cards, headers) into separate components
- **Page components** - Keep page-level components in `src/components/` with descriptive names
- **Shared components** - Consider a `src/components/shared/` folder for reusable UI elements

## File Naming

- **Pages**: `Home.tsx`, `About.tsx`, `Contact.tsx` (PascalCase)
- **Components**: `Button.tsx`, `Card.tsx`, `Header.tsx` (PascalCase)
- **Utilities**: `helpers.ts`, `constants.ts` (camelCase)
- **Styles**: Match component name - `Home.css`, `Button.module.css`

## Code Organization

Keep related files together:
```
src/components/
├── Home/
│   ├── Home.tsx
│   ├── Home.css
│   └── HomeHero.tsx      # Sub-component used only by Home
├── About/
│   ├── About.tsx
│   └── About.css
└── shared/
    ├── Button.tsx
    ├── Card.tsx
    └── Header.tsx
```
