# Screenshot Guidelines for How-To Documentation

## Purpose

Screenshots are the backbone of effective how-to guides. This guide ensures your screenshots are clear, consistent, and helpful.

---

## When to Include Screenshots

### ✅ Always Include Screenshots For:

- **Complex interfaces** - Multi-tab systems, dense forms
- **First-time user steps** - Login screens, first navigation
- **Critical decision points** - "Click this, not that"
- **Success/confirmation states** - "Here's what you should see"
- **Error messages** - Show the actual error users will encounter
- **Form fields** - Especially with many required fields
- **Navigation paths** - Menu sequences, tab selections
- **Before/after comparisons** - Show the result of an action

### ❌ Skip Screenshots For:

- **Obvious actions** - "Open your browser" (unless showing specific browser)
- **Repetitive steps** - Show once, then refer back to it
- **Text-only instructions** - "Enter your email address" doesn't need a screenshot
- **Common UI patterns** - Everyone knows what a checkbox looks like
- **Rapidly changing content** - Screenshots will become outdated quickly

### Decision Rule:

Ask: "Would a first-time user be confused without this image?" If yes, include it.

---

## Screenshot Best Practices

### Capture Quality

**Resolution:**
- Capture at **1920x1080** (full HD) minimum
- Use native/actual resolution of your screen
- Don't scale up lower-resolution images

**File Format:**
- **PNG** for all UI screenshots (lossless, supports transparency)
- **JPG** only for photographs or when file size is critical
- Avoid GIF (except for animated sequences)

**File Size:**
- Optimize before uploading (use tools like TinyPNG)
- Target: under 500KB per image when possible
- Notion auto-optimizes on upload, but start with quality

### Capture Tools

**Recommended Tools:**

**macOS:**
- Built-in: `Cmd + Shift + 4` (selection) or `Cmd + Shift + 3` (full screen)
- Advanced: CleanShot X, Snagit

**Windows:**
- Built-in: `Win + Shift + S` (Snipping Tool)
- Advanced: Snagit, Greenshot

**Browser Extensions:**
- Awesome Screenshot
- Fireshot (for full-page captures)

**Cross-platform:**
- Snagit (paid, excellent annotation tools)
- ShareX (Windows, free, powerful)

---

## What to Capture

### Show Only What's Relevant

**Good Cropping:**
- ✅ Include the element being described
- ✅ Include enough context (nearby labels, headings)
- ✅ Exclude unnecessary browser chrome, taskbars
- ✅ Keep aspect ratio reasonable (not too wide or tall)

**Bad Cropping:**
- ❌ Capturing entire 4K screen when showing one button
- ❌ Cutting off labels or field names
- ❌ Including personal information (names, emails, IDs)
- ❌ Including irrelevant browser tabs or bookmarks

### Privacy & Security

**Always Remove:**
- Real employee names (unless they're test accounts)
- Employee IDs or personal identifiers
- Email addresses (use example@example.com)
- Phone numbers
- Real financial data, SSNs, medical info
- Proprietary business information

**How to Redact:**
- Use solid rectangles (not translucent)
- Match the background color when possible
- Use [REDACTED] or dummy data before capturing
- Or use a test/demo environment

---

## Annotation Best Practices

### When to Annotate

**Use annotations to:**
- Draw attention to specific UI elements
- Show the sequence of actions (numbered steps)
- Highlight required fields
- Indicate clickable areas
- Show relationships between elements

**Don't annotate if:**
- The screenshot is already clear
- The text instructions are sufficient
- Over-annotation would clutter the image

### Annotation Tools & Techniques

**Basic Annotations:**

**Arrows:**
- Use to point to specific elements
- Keep arrows simple and clear
- Red for "click here" or critical actions
- Green for success indicators
- Blue for informational callouts

**Boxes/Rectangles:**
- Outline important sections
- Highlight required fields
- Show active/selected states
- Red border for focus, green for success

**Numbers:**
- Show sequence of actions (1, 2, 3)
- Use circles with numbers inside
- Place near the element, not covering it

**Text Labels:**
- Use sparingly - prefer callouts in the document
- Keep text large enough to read (16pt minimum)
- Use high contrast (white text on dark background)

**Color Guidelines:**
- 🔴 **Red:** Attention, required, critical, "click here"
- 🟢 **Green:** Success, correct, approved, "looks like this"
- 🟡 **Yellow:** Caution, optional, note
- 🔵 **Blue:** Information, reference, navigation
- ⚫ **Black/Gray:** Neutral annotations

### Annotation Style Consistency

**Across all your screenshots:**
- Use the same arrow style
- Use the same number circle style
- Use the same colors for same purposes
- Use the same font for text annotations
- Keep annotation stroke width consistent

---

## Screenshot Placement in Documents

### Positioning

**Best Practice:**
Place screenshots **immediately after** the step they illustrate.

**Good flow:**
```
1. Click the **Save** button in the top-right corner.

[Screenshot showing Save button highlighted]

Expected Result: You'll see a green confirmation message.
```

**Poor flow:**
```
1. Click the **Save** button.
2. Review the confirmation.
3. Click **Close**.

[Screenshot showing Save button - too far from step 1]
```

### Sizing

**In Notion:**
- Default width works for most screenshots
- Expand to full width for wide interface screenshots
- Reduce size for small UI elements or icons
- Keep consistent sizes within same document

**For PDF Export:**
- Test that images aren't pixelated when printed
- Ensure text in screenshots is readable
- Check that nothing is cut off at page breaks

### Captions

**When to add captions:**
- Complex screenshots needing explanation
- Before/after comparisons
- Screenshots showing expected results
- Error message screenshots

**Caption format:**
- Keep brief (one sentence)
- Use italics to distinguish from body text
- Place directly below the image

**Example:**
```
[Screenshot]

*The status indicator should turn green when the upload is complete.*
```

---

## Special Screenshot Types

### Form Screenshots

**Best practices:**
- Show empty form (what user will see)
- Show completed form (example of correct entries)
- Highlight required fields with red boxes or asterisks
- Include field labels in the capture

**Annotations:**
- Number fields in the order they should be filled
- Mark required fields with red asterisks
- Show field format examples (dates, phone numbers)

### Error Screenshots

**Capture:**
- The entire error message (all text)
- Any error codes or reference numbers
- The UI state that caused the error
- Relevant context (what the user was trying to do)

**Annotations:**
- Highlight the error message itself
- Draw attention to the solution if visible on screen
- Show related fields that may need correction

### Navigation Path Screenshots

**For menu sequences (File > Edit > Settings):**

**Option 1:** Single screenshot with numbered annotations
1. First click location
2. Second click location
3. Final selection

**Option 2:** Multiple small screenshots in sequence

**Option 3:** Animated GIF (for complex multi-step navigation)

### Before/After Screenshots

**Side-by-side comparison:**
- Use Notion's column feature
- Label clearly: "Before" and "After"
- Ensure both screenshots are the same size
- Highlight the change with annotations

---

## Mobile & Responsive Screenshots

### Device Screenshots

**For mobile apps or responsive web:**
- Use device frames (iPhone, Android) for context
- Show actual device size, don't enlarge excessively
- Capture at native resolution
- Use device mockup tools for polish

**Tools:**
- Mockup generators: Mockuphone, Placeit
- Device screenshots: iOS Simulator, Android Emulator
- Browser DevTools device mode

### Different Screen Sizes

If your guide covers responsive design:
- Show desktop view first
- Include mobile view for significantly different UI
- Note which screenshots are from mobile
- Explain differences between views

---

## Screenshot Update & Maintenance

### When to Update Screenshots

**Immediately update when:**
- UI design changes significantly
- Button labels or menu items change
- Error messages are reworded
- New features are added to the interface
- Company branding changes

**Schedule regular reviews:**
- Quarterly check for UI changes
- After every major system update
- When users report confusion
- Annually for stable systems

### Version Control

**Track screenshot versions:**
- Save original, unedited screenshots
- Use descriptive filenames: `step-3-save-button-v2.png`
- Date screenshots: `login-screen-2024-10-21.png`
- Keep a screenshot library organized by guide

### Efficient Batch Updates

**When UI changes affect multiple guides:**
1. List all affected guides
2. Retake all necessary screenshots in one session
3. Update all guides before releasing any
4. Test the guides with screenshots
5. Publish updates simultaneously

---

## Animated Screenshots (GIFs)

### When to Use Animated GIFs

**Good uses:**
- Complex multi-step sequences
- Drag-and-drop operations
- Hover states and transitions
- Interactive elements
- Navigation flows

**Avoid for:**
- Simple click actions
- Static forms
- Anything that can be shown in one image

### Creating GIFs

**Tools:**
- **LICEcap** (lightweight, simple)
- **ScreenToGif** (Windows, powerful)
- **Kap** (Mac, modern interface)
- **Gifox** (Mac, polished output)

**Best practices:**
- Keep under 10 seconds
- Optimize file size (under 5MB)
- Loop continuously
- Add pause at end before loop
- Show cursor clearly
- Use smooth, deliberate movements

---

## Accessibility Considerations

### Alt Text

**For complex diagrams or important screenshots:**
- Provide descriptive alt text
- Explain what's shown in the image
- Describe the action being demonstrated
- Note: Not all platforms support alt text in all contexts

### Don't Rely on Color Alone

- Use shapes, patterns, labels in addition to color
- Ensure sufficient contrast (text in screenshots)
- Test with colorblind simulation tools

### Make Screenshots Supplementary

- Text instructions should be complete without screenshots
- Screenshots enhance but don't replace text
- Consider users with screen readers

---

## Common Screenshot Mistakes

### ❌ Mistake: Including Personal Information

**Problem:** Real employee data in screenshots

**Solution:** Use test accounts, blur sensitive info, or use mockups

---

### ❌ Mistake: Too Much Content

**Problem:** Full-page screenshot when showing one button

**Solution:** Crop tightly to relevant area

---

### ❌ Mistake: Inconsistent Style

**Problem:** Different annotation colors and styles in same guide

**Solution:** Create an annotation template and stick to it

---

### ❌ Mistake: Outdated Screenshots

**Problem:** UI has changed but screenshots haven't been updated

**Solution:** Set calendar reminders to review quarterly

---

### ❌ Mistake: Poor Quality

**Problem:** Blurry, pixelated, or too-dark screenshots

**Solution:** Capture at higher resolution, adjust brightness/contrast

---

### ❌ Mistake: No Context

**Problem:** Zoomed in so close that users can't find the element

**Solution:** Include surrounding UI elements, labels, headings

---

### ❌ Mistake: Over-Annotation

**Problem:** So many arrows and boxes that screenshot is cluttered

**Solution:** Use fewer, more purposeful annotations

---

## Screenshot Checklist

Before adding a screenshot to your guide:

- [ ] Screenshot is clear and high-resolution
- [ ] Cropped to show only relevant content
- [ ] No personal or sensitive information visible
- [ ] Annotations are clear and purposeful
- [ ] Consistent with other screenshots in guide
- [ ] Placed immediately after relevant step
- [ ] File size is optimized
- [ ] Readable text (not too small)
- [ ] Good contrast and visibility
- [ ] Tests well in PDF export

---

## Tools & Resources

### Screenshot Capture
- **Mac:** Cmd + Shift + 4 (built-in)
- **Windows:** Win + Shift + S (Snipping Tool)
- **CleanShot X:** Advanced Mac screenshot tool
- **Snagit:** Cross-platform, annotation-friendly

### Annotation
- **Snagit:** Comprehensive annotation tools
- **Skitch:** Simple, free annotations
- **Markup (Mac):** Built-in Preview tool
- **Paint 3D (Windows):** Built-in tool

### Optimization
- **TinyPNG:** Web-based image compressor
- **ImageOptim (Mac):** Drag-and-drop optimizer
- **FileOptimizer (Windows):** Batch compression

### Mockups & Device Frames
- **Mockuphone:** Device frame generator
- **Figma:** Design tool with device templates
- **Placeit:** Professional mockups

### Screen Recording → GIF
- **LICEcap:** Simple, lightweight
- **Gifox (Mac):** Beautiful GIFs
- **ScreenToGif (Windows):** Feature-rich

---

*Last Updated: October 2025*  
*For questions about screenshot best practices, contact [documentation team]*
