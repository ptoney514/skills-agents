# Example: Personal Project UI Library

This example shows how to build a reusable design system for your personal projects.

---

## Scenario

**Goal:** Create a consistent UI library you can use across multiple personal projects
**Aesthetic:** Modern, minimal, professional
**Projects:** Portfolio site, side projects, SaaS experiments
**Tech Stack:** Next.js, React, TypeScript, Tailwind CSS

---

## Step-by-Step Workflow

### Step 1: Invoke the Agent

```
I want to create a personal design system that I can reuse across all my projects.
Can you use the design-systems-engineer agent to help?

I like modern, minimal aesthetics. Clean, professional, with pops of color.
Think: Vercel, Linear, Stripe vibes.

I need basic components: buttons, forms, cards, and maybe a few layout components.
```

---

### Step 2: Agent Proposes Design Direction

**Agent:** "Let me propose a modern, minimal design system for you:

**Color Palette:**
- **Primary:** Indigo (for CTAs and interactive elements)
- **Neutral:** True grays (for text and backgrounds)
- **Accent:** Amber (for highlights and success states)
- **Semantic colors:** Success (green), warning (yellow), error (red)

**Typography:**
- **Headings:** Inter (900 weight for bold impact)
- **Body:** Inter (400-500 for readability)
- **Mono:** JetBrains Mono (for code snippets)

**Aesthetic:**
- Subtle shadows for depth
- Generous white space
- Rounded corners (modern but not playful)
- High contrast for accessibility

Does this direction resonate with you?"

**You:** "Yes! Love it. Let's go with that."

---

### Step 3: Design Token Setup

**Agent creates:** `tailwind.config.ts`

```typescript
import type { Config } from 'tailwindcss'

const config: Config = {
  darkMode: ['class'],
  content: [
    './pages/**/*.{ts,tsx}',
    './components/**/*.{ts,tsx}',
    './app/**/*.{ts,tsx}',
    './src/**/*.{ts,tsx}',
  ],
  theme: {
    container: {
      center: true,
      padding: '2rem',
      screens: {
        '2xl': '1400px',
      },
    },
    extend: {
      colors: {
        // Personal Brand Colors
        border: 'hsl(var(--border))',
        input: 'hsl(var(--input))',
        ring: 'hsl(var(--ring))',
        background: 'hsl(var(--background))',
        foreground: 'hsl(var(--foreground))',
        primary: {
          DEFAULT: 'hsl(var(--primary))',
          foreground: 'hsl(var(--primary-foreground))',
        },
        secondary: {
          DEFAULT: 'hsl(var(--secondary))',
          foreground: 'hsl(var(--secondary-foreground))',
        },
        destructive: {
          DEFAULT: 'hsl(var(--destructive))',
          foreground: 'hsl(var(--destructive-foreground))',
        },
        muted: {
          DEFAULT: 'hsl(var(--muted))',
          foreground: 'hsl(var(--muted-foreground))',
        },
        accent: {
          DEFAULT: 'hsl(var(--accent))',
          foreground: 'hsl(var(--accent-foreground))',
        },
        popover: {
          DEFAULT: 'hsl(var(--popover))',
          foreground: 'hsl(var(--popover-foreground))',
        },
        card: {
          DEFAULT: 'hsl(var(--card))',
          foreground: 'hsl(var(--card-foreground))',
        },
      },
      borderRadius: {
        lg: 'var(--radius)',
        md: 'calc(var(--radius) - 2px)',
        sm: 'calc(var(--radius) - 4px)',
      },
      fontFamily: {
        sans: ['Inter', 'system-ui', 'sans-serif'],
        mono: ['JetBrains Mono', 'monospace'],
      },
      keyframes: {
        'accordion-down': {
          from: { height: '0' },
          to: { height: 'var(--radix-accordion-content-height)' },
        },
        'accordion-up': {
          from: { height: 'var(--radix-accordion-content-height)' },
          to: { height: '0' },
        },
      },
      animation: {
        'accordion-down': 'accordion-down 0.2s ease-out',
        'accordion-up': 'accordion-up 0.2s ease-out',
      },
    },
  },
  plugins: [require('tailwindcss-animate')],
}

export default config
```

**Agent creates:** `src/styles/globals.css`

```css
@tailwind base;
@tailwind components;
@tailwind utilities;

@layer base {
  :root {
    --background: 0 0% 100%;
    --foreground: 222.2 84% 4.9%;

    --card: 0 0% 100%;
    --card-foreground: 222.2 84% 4.9%;

    --popover: 0 0% 100%;
    --popover-foreground: 222.2 84% 4.9%;

    --primary: 239 84% 67%;
    --primary-foreground: 0 0% 100%;

    --secondary: 210 40% 96.1%;
    --secondary-foreground: 222.2 47.4% 11.2%;

    --muted: 210 40% 96.1%;
    --muted-foreground: 215.4 16.3% 46.9%;

    --accent: 45 93% 47%;
    --accent-foreground: 0 0% 100%;

    --destructive: 0 84.2% 60.2%;
    --destructive-foreground: 0 0% 100%;

    --border: 214.3 31.8% 91.4%;
    --input: 214.3 31.8% 91.4%;
    --ring: 239 84% 67%;

    --radius: 0.5rem;
  }

  .dark {
    --background: 222.2 84% 4.9%;
    --foreground: 210 40% 98%;

    --card: 222.2 84% 4.9%;
    --card-foreground: 210 40% 98%;

    --popover: 222.2 84% 4.9%;
    --popover-foreground: 210 40% 98%;

    --primary: 239 84% 67%;
    --primary-foreground: 0 0% 100%;

    --secondary: 217.2 32.6% 17.5%;
    --secondary-foreground: 210 40% 98%;

    --muted: 217.2 32.6% 17.5%;
    --muted-foreground: 215 20.2% 65.1%;

    --accent: 45 93% 47%;
    --accent-foreground: 0 0% 100%;

    --destructive: 0 62.8% 30.6%;
    --destructive-foreground: 210 40% 98%;

    --border: 217.2 32.6% 17.5%;
    --input: 217.2 32.6% 17.5%;
    --ring: 239 84% 67%;
  }
}

@layer base {
  * {
    @apply border-border;
  }
  body {
    @apply bg-background text-foreground;
  }
}
```

---

### Step 4: Install Core Components

**Agent runs:**

```bash
npx shadcn-ui@latest init
npx shadcn-ui@latest add button
npx shadcn-ui@latest add card
npx shadcn-ui@latest add input
npx shadcn-ui@latest add label
npx shadcn-ui@latest add badge
npx shadcn-ui@latest add avatar
npx shadcn-ui@latest add separator
```

---

### Step 5: Custom Composite Component - Feature Card

**Agent creates:** `src/components/custom/FeatureCard.tsx`

```typescript
import { Card, CardHeader, CardTitle, CardDescription, CardContent } from '@/components/ui/card'
import { Badge } from '@/components/ui/badge'
import { LucideIcon } from 'lucide-react'

interface FeatureCardProps {
  icon: LucideIcon
  title: string
  description: string
  badge?: string
  action?: React.ReactNode
}

export function FeatureCard({
  icon: Icon,
  title,
  description,
  badge,
  action,
}: FeatureCardProps) {
  return (
    <Card className="group hover:shadow-lg transition-all duration-200 hover:border-primary/50">
      <CardHeader>
        <div className="flex items-start justify-between">
          <div className="p-2 rounded-lg bg-primary/10 text-primary mb-4">
            <Icon className="h-6 w-6" />
          </div>
          {badge && (
            <Badge variant="secondary" className="font-mono text-xs">
              {badge}
            </Badge>
          )}
        </div>
        <CardTitle className="group-hover:text-primary transition-colors">
          {title}
        </CardTitle>
        <CardDescription className="text-base">{description}</CardDescription>
      </CardHeader>
      {action && <CardContent>{action}</CardContent>}
    </Card>
  )
}
```

---

### Step 6: Create Component Showcase

**Agent creates:** `app/components/page.tsx`

```typescript
import { Button } from '@/components/ui/button'
import { Card, CardHeader, CardTitle, CardDescription, CardContent } from '@/components/ui/card'
import { Input } from '@/components/ui/input'
import { Label } from '@/components/ui/label'
import { Badge } from '@/components/ui/badge'
import { FeatureCard } from '@/components/custom/FeatureCard'
import { Zap, Lock, Globe } from 'lucide-react'

export default function ComponentsPage() {
  return (
    <div className="container mx-auto py-12 space-y-16">
      {/* Header */}
      <div className="space-y-4">
        <h1 className="text-4xl font-bold">Design System</h1>
        <p className="text-xl text-muted-foreground">
          Reusable components for all my projects
        </p>
      </div>

      {/* Colors */}
      <section className="space-y-4">
        <h2 className="text-2xl font-bold">Colors</h2>
        <div className="grid grid-cols-2 md:grid-cols-4 gap-4">
          <div className="space-y-2">
            <div className="h-24 rounded-lg bg-primary" />
            <p className="font-mono text-sm">Primary</p>
          </div>
          <div className="space-y-2">
            <div className="h-24 rounded-lg bg-secondary" />
            <p className="font-mono text-sm">Secondary</p>
          </div>
          <div className="space-y-2">
            <div className="h-24 rounded-lg bg-accent" />
            <p className="font-mono text-sm">Accent</p>
          </div>
          <div className="space-y-2">
            <div className="h-24 rounded-lg bg-destructive" />
            <p className="font-mono text-sm">Destructive</p>
          </div>
        </div>
      </section>

      {/* Buttons */}
      <section className="space-y-4">
        <h2 className="text-2xl font-bold">Buttons</h2>
        <div className="flex flex-wrap gap-4">
          <Button>Primary Button</Button>
          <Button variant="secondary">Secondary</Button>
          <Button variant="outline">Outline</Button>
          <Button variant="ghost">Ghost</Button>
          <Button variant="destructive">Destructive</Button>
        </div>
      </section>

      {/* Feature Cards */}
      <section className="space-y-4">
        <h2 className="text-2xl font-bold">Feature Cards</h2>
        <div className="grid md:grid-cols-3 gap-6">
          <FeatureCard
            icon={Zap}
            title="Fast Performance"
            description="Built with speed in mind"
            badge="NEW"
          />
          <FeatureCard
            icon={Lock}
            title="Secure by Default"
            description="Industry-standard security"
          />
          <FeatureCard
            icon={Globe}
            title="Global CDN"
            description="Deployed worldwide"
          />
        </div>
      </section>

      {/* Forms */}
      <section className="space-y-4">
        <h2 className="text-2xl font-bold">Forms</h2>
        <Card className="max-w-md">
          <CardHeader>
            <CardTitle>Login</CardTitle>
            <CardDescription>Enter your credentials</CardDescription>
          </CardHeader>
          <CardContent className="space-y-4">
            <div className="space-y-2">
              <Label htmlFor="email">Email</Label>
              <Input id="email" type="email" placeholder="you@example.com" />
            </div>
            <div className="space-y-2">
              <Label htmlFor="password">Password</Label>
              <Input id="password" type="password" />
            </div>
            <Button className="w-full">Sign In</Button>
          </CardContent>
        </Card>
      </section>
    </div>
  )
}
```

---

### Step 7: Reusable Pattern Library

**Agent creates:** `docs/patterns.md`

Documents reusable patterns you can copy-paste into any project:

- Hero sections
- Feature grids
- Pricing tables
- Testimonial cards
- Footer layouts

---

## Final Structure

```
personal-ui-library/
├── tailwind.config.ts           ✅ Design tokens (reusable!)
├── src/
│   ├── components/
│   │   ├── ui/                  ✅ shadcn/ui base components
│   │   │   ├── button.tsx
│   │   │   ├── card.tsx
│   │   │   ├── input.tsx
│   │   │   └── ...
│   │   └── custom/              ✅ Your custom components
│   │       ├── FeatureCard.tsx
│   │       ├── HeroSection.tsx
│   │       └── ...
│   └── styles/
│       └── globals.css          ✅ Design tokens as CSS vars
├── app/
│   └── components/
│       └── page.tsx             ✅ Live showcase
└── docs/
    └── patterns.md              ✅ Reusable patterns
```

---

## Reusing Across Projects

**For a new project:**

1. **Copy design tokens:**
   ```bash
   cp tailwind.config.ts ../new-project/
   cp src/styles/globals.css ../new-project/src/styles/
   ```

2. **Copy components you need:**
   ```bash
   cp -r src/components/ui ../new-project/src/components/
   cp src/components/custom/FeatureCard.tsx ../new-project/src/components/custom/
   ```

3. **Install dependencies:**
   ```bash
   npm install tailwindcss-animate class-variance-authority clsx tailwind-merge
   ```

4. **You're ready to build!**

---

## Timeline

- **Discovery & Design Direction:** 10 minutes
- **Design Token Setup:** 15 minutes
- **Component Installation:** 20 minutes
- **Custom Components:** 30 minutes
- **Showcase Page:** 20 minutes
- **Pattern Documentation:** 15 minutes

**Total: ~2 hours** for complete personal design system

---

## Benefits

Now you have:

✅ **Consistent brand** across all your projects
✅ **Rapid prototyping** - Just copy components
✅ **Professional quality** - Production-ready code
✅ **Dark mode** - Built in!
✅ **Accessible** - WCAG AA compliant
✅ **Type-safe** - Full TypeScript support

---

**Result:** A reusable, professional design system you can deploy in minutes for any new project!
