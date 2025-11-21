# Example: Client Project Design System

This example shows how to use the Design Systems Engineer agent for a client project.

---

## Scenario

**Client:** HealthTrack Medical Software
**Project:** Patient portal redesign
**Requirements:**
- Brand colors: Blue (#0066CC), Green (#00B894), Gray (#2D3436)
- Font: Inter for UI, Merriweather for headings
- Components needed: Forms, data tables, patient cards, appointment scheduler
- Accessibility: WCAG AA compliance (medical software requirement)

---

## Step-by-Step Workflow

### Step 1: Invoke the Agent

```
I'm building a design system for a healthcare client called HealthTrack.
Please use the design-systems-engineer agent to help me.

Here are the brand guidelines:
- Primary color: #0066CC (Medical Blue)
- Success color: #00B894 (Healing Green)
- Text color: #2D3436 (Charcoal)
- Font: Inter for UI, Merriweather for headings
- Style: Professional, clean, trustworthy

I need: buttons, forms, patient cards, and data tables.
```

---

### Step 2: Agent Discovery Phase

The agent will ask clarifying questions:

**Agent:** "Let me make sure I understand your requirements:

1. What platforms? (Web only, or mobile-web responsive?)
2. Do you have existing Figma designs, or should I create design tokens from these specs?
3. Any specific accessibility requirements beyond WCAG AA?
4. What's the primary use case for the data tables? (Patient lists, appointment schedules, medical records?)
5. Do you need dark mode support?"

**You respond:**
- Web only, but fully responsive (mobile, tablet, desktop)
- No Figma yet, create tokens from specs
- WCAG AA is sufficient
- Data tables for patient lists and appointment schedules
- No dark mode needed

---

### Step 3: Design Token Creation

**Agent creates:** `tailwind.config.js`

```typescript
import type { Config } from 'tailwindcss'

const config: Config = {
  content: [
    './pages/**/*.{js,ts,jsx,tsx,mdx}',
    './components/**/*.{js,ts,jsx,tsx,mdx}',
    './app/**/*.{js,ts,jsx,tsx,mdx}',
  ],
  theme: {
    extend: {
      colors: {
        // HealthTrack Brand Colors
        primary: {
          50: '#E6F2FF',
          100: '#CCE5FF',
          200: '#99CBFF',
          300: '#66B2FF',
          400: '#3398FF',
          500: '#0066CC', // Brand primary
          600: '#0052A3',
          700: '#003D7A',
          800: '#002952',
          900: '#001429',
        },
        success: {
          50: '#E6FFF9',
          100: '#CCFFF3',
          200: '#99FFE7',
          300: '#66FFDB',
          400: '#33FFCF',
          500: '#00B894', // Brand success
          600: '#009376',
          700: '#006E58',
          800: '#004A3B',
          900: '#00251D',
        },
        neutral: {
          50: '#F8F9FA',
          100: '#E9ECEF',
          200: '#DEE2E6',
          300: '#CED4DA',
          400: '#ADB5BD',
          500: '#6C757D',
          600: '#495057',
          700: '#343A40',
          800: '#2D3436', // Brand text
          900: '#1A1D1F',
        },
      },
      fontFamily: {
        sans: ['Inter', 'system-ui', 'sans-serif'],
        serif: ['Merriweather', 'Georgia', 'serif'],
      },
      fontSize: {
        // Medical UI needs clear hierarchy
        'xs': ['0.75rem', { lineHeight: '1rem' }],
        'sm': ['0.875rem', { lineHeight: '1.25rem' }],
        'base': ['1rem', { lineHeight: '1.5rem' }],
        'lg': ['1.125rem', { lineHeight: '1.75rem' }],
        'xl': ['1.25rem', { lineHeight: '1.75rem' }],
        '2xl': ['1.5rem', { lineHeight: '2rem' }],
        '3xl': ['1.875rem', { lineHeight: '2.25rem' }],
      },
      spacing: {
        // 4px base scale for precise medical UI
        '18': '4.5rem',
        '88': '22rem',
      },
      borderRadius: {
        'sm': '0.25rem',
        'DEFAULT': '0.5rem',
        'md': '0.5rem',
        'lg': '0.75rem',
        'xl': '1rem',
      },
      boxShadow: {
        'sm': '0 1px 2px 0 rgb(0 0 0 / 0.05)',
        'DEFAULT': '0 1px 3px 0 rgb(0 0 0 / 0.1), 0 1px 2px -1px rgb(0 0 0 / 0.1)',
        'md': '0 4px 6px -1px rgb(0 0 0 / 0.1), 0 2px 4px -2px rgb(0 0 0 / 0.1)',
        'lg': '0 10px 15px -3px rgb(0 0 0 / 0.1), 0 4px 6px -4px rgb(0 0 0 / 0.1)',
      },
    },
  },
  plugins: [],
}

export default config
```

**Agent provides:** Documentation explaining token usage

---

### Step 4: Component Installation

**Agent installs shadcn/ui components:**

```bash
npx shadcn-ui@latest add button
npx shadcn-ui@latest add input
npx shadcn-ui@latest add label
npx shadcn-ui@latest add card
npx shadcn-ui@latest add table
npx shadcn-ui@latest add select
npx shadcn-ui@latest add checkbox
```

---

### Step 5: Custom Component - Patient Card

**Agent creates:** `src/components/custom/PatientCard.tsx`

```typescript
import { Card, CardHeader, CardTitle, CardDescription, CardContent } from '@/components/ui/card'
import { Badge } from '@/components/ui/badge'
import { Avatar, AvatarFallback, AvatarImage } from '@/components/ui/avatar'

interface PatientCardProps {
  patientId: string
  name: string
  age: number
  gender: 'M' | 'F' | 'Other'
  status: 'active' | 'inactive' | 'pending'
  lastVisit: string
  avatarUrl?: string
}

export function PatientCard({
  patientId,
  name,
  age,
  gender,
  status,
  lastVisit,
  avatarUrl,
}: PatientCardProps) {
  const getStatusColor = (status: string) => {
    switch (status) {
      case 'active':
        return 'bg-success-500 text-white'
      case 'pending':
        return 'bg-yellow-500 text-white'
      case 'inactive':
        return 'bg-neutral-400 text-white'
      default:
        return 'bg-neutral-400 text-white'
    }
  }

  const initials = name
    .split(' ')
    .map((n) => n[0])
    .join('')
    .toUpperCase()

  return (
    <Card className="hover:shadow-md transition-shadow">
      <CardHeader className="flex flex-row items-center gap-4">
        <Avatar className="h-12 w-12">
          <AvatarImage src={avatarUrl} alt={name} />
          <AvatarFallback className="bg-primary-100 text-primary-700">
            {initials}
          </AvatarFallback>
        </Avatar>
        <div className="flex-1">
          <CardTitle className="font-serif text-lg">{name}</CardTitle>
          <CardDescription>ID: {patientId}</CardDescription>
        </div>
        <Badge className={getStatusColor(status)}>
          {status.toUpperCase()}
        </Badge>
      </CardHeader>
      <CardContent>
        <dl className="grid grid-cols-2 gap-2 text-sm">
          <dt className="text-neutral-600">Age:</dt>
          <dd className="font-medium">{age} years</dd>
          <dt className="text-neutral-600">Gender:</dt>
          <dd className="font-medium">{gender}</dd>
          <dt className="text-neutral-600">Last Visit:</dt>
          <dd className="font-medium">{lastVisit}</dd>
        </dl>
      </CardContent>
    </Card>
  )
}
```

---

### Step 6: Component Showcase Page

**Agent creates:** `app/design-system/page.tsx`

Shows all components with interactive examples, proper spacing, and copy-paste code snippets.

---

### Step 7: Documentation Handoff

**Agent provides:**

1. **Design System Guide** (`docs/design-system.md`)
   - Token usage and semantic meaning
   - Component API reference
   - Accessibility guidelines
   - Responsive behavior

2. **Contribution Guidelines** (`docs/contributing.md`)
   - How to add new components
   - Component checklist
   - Code review process

3. **Brand Guidelines Integration** (`docs/brand-integration.md`)
   - How HealthTrack brand maps to design tokens
   - Typography usage rules
   - Color semantic meanings

---

## Final Deliverables

```
healthtrack-portal/
├── tailwind.config.ts           ✅ Brand design tokens
├── src/
│   ├── components/
│   │   ├── ui/                  ✅ shadcn/ui components (customized)
│   │   │   ├── button.tsx
│   │   │   ├── card.tsx
│   │   │   ├── input.tsx
│   │   │   ├── table.tsx
│   │   │   └── ...
│   │   └── custom/              ✅ HealthTrack-specific components
│   │       ├── PatientCard.tsx
│   │       ├── AppointmentScheduler.tsx
│   │       └── PatientTable.tsx
│   └── styles/
│       └── globals.css          ✅ Tailwind imports + custom styles
├── app/
│   └── design-system/
│       └── page.tsx             ✅ Component showcase
└── docs/
    ├── design-system.md         ✅ Design system guide
    ├── contributing.md          ✅ Contribution guidelines
    └── brand-integration.md     ✅ Brand mapping document
```

---

## Timeline

- **Discovery & Planning:** 15 minutes
- **Design Token Setup:** 20 minutes
- **Component Installation & Customization:** 1.5 hours
- **Custom Components (PatientCard, Table, etc.):** 1 hour
- **Showcase Page:** 30 minutes
- **Documentation:** 30 minutes

**Total: ~3.5 hours** for complete, production-ready design system

---

## Client Handoff

When handing off to HealthTrack's development team:

1. **Demo the showcase page** - Show all components interactively
2. **Walk through design tokens** - Explain color semantic meanings
3. **Review accessibility** - Demonstrate keyboard navigation, screen reader support
4. **Provide documentation** - Give them design system guide and component APIs
5. **Set up contribution process** - Show how to add new components following standards

---

**Result:** HealthTrack has a complete, branded, accessible design system ready for their patient portal development.
