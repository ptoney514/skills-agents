import * as React from 'react'
import { cva, type VariantProps } from 'class-variance-authority'
import { cn } from '@/lib/utils'

// Define component variants using class-variance-authority
const componentVariants = cva(
  // Base styles (always applied)
  'inline-flex items-center justify-center rounded-md text-sm font-medium transition-colors focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-ring focus-visible:ring-offset-2 disabled:opacity-50 disabled:pointer-events-none',
  {
    variants: {
      // Variant: Different visual styles
      variant: {
        default: 'bg-primary text-primary-foreground hover:bg-primary/90',
        secondary: 'bg-secondary text-secondary-foreground hover:bg-secondary/80',
        outline: 'border border-input hover:bg-accent hover:text-accent-foreground',
        ghost: 'hover:bg-accent hover:text-accent-foreground',
        destructive: 'bg-destructive text-destructive-foreground hover:bg-destructive/90',
      },
      // Size: Different component sizes
      size: {
        sm: 'h-9 px-3',
        default: 'h-10 py-2 px-4',
        lg: 'h-11 px-8',
        icon: 'h-10 w-10',
      },
    },
    defaultVariants: {
      variant: 'default',
      size: 'default',
    },
  }
)

// Component props interface
export interface ComponentProps
  extends React.HTMLAttributes<HTMLDivElement>,
    VariantProps<typeof componentVariants> {
  // Add custom props here
  asChild?: boolean
  disabled?: boolean
}

// Component implementation
const Component = React.forwardRef<HTMLDivElement, ComponentProps>(
  ({ className, variant, size, asChild = false, disabled, ...props }, ref) => {
    // Component logic here

    return (
      <div
        ref={ref}
        className={cn(componentVariants({ variant, size, className }))}
        aria-disabled={disabled}
        {...props}
      />
    )
  }
)

Component.displayName = 'Component'

export { Component, componentVariants }

// Example usage:
//
// import { Component } from '@/components/ui/component'
//
// export default function Example() {
//   return (
//     <div>
//       {/* Default variant and size */}
//       <Component>Default Component</Component>
//
//       {/* Secondary variant, large size */}
//       <Component variant="secondary" size="lg">
//         Secondary Large
//       </Component>
//
//       {/* Outline variant, small size */}
//       <Component variant="outline" size="sm">
//         Outline Small
//       </Component>
//
//       {/* Disabled state */}
//       <Component disabled>
//         Disabled Component
//       </Component>
//     </div>
//   )
// }
