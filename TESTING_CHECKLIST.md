# ✅ Dashboard v2 Testing Checklist

## 🖥️ Desktop Testing

### Initial Load
- [ ] Open http://localhost:8317/dashboard-v2.html
- [ ] Page loads without errors
- [ ] Stats cards display correctly
- [ ] Quota cards show data
- [ ] Chart renders properly
- [ ] v2.0 badge visible (top right)

### Theme Toggle
- [ ] Click 🌓 button in header
- [ ] Theme switches to light mode
- [ ] All colors update properly
- [ ] Chart colors adjust
- [ ] Click again to switch back to dark
- [ ] Theme persists on page reload

### Auto-Refresh
- [ ] Auto-refresh checkbox is checked by default
- [ ] Countdown timer shows 30...29...28... seconds
- [ ] After 30 seconds, data refreshes automatically
- [ ] Countdown resets to 30
- [ ] Uncheck auto-refresh checkbox
- [ ] Countdown shows "-"
- [ ] Data doesn't auto-refresh anymore
- [ ] Check auto-refresh again to re-enable

### Manual Refresh
- [ ] Click "🔄 Refresh" button
- [ ] Button shows "⏳ Loading..."
- [ ] Data updates
- [ ] Button returns to "🔄 Refresh"
- [ ] Countdown resets (if auto-refresh enabled)

### Chart Interaction
- [ ] Scroll down to see chart
- [ ] Chart displays 4 bars (Gemini Pro, Claude, Flash, Image)
- [ ] Bars are color-coded
- [ ] Hover over bars shows tooltip
- [ ] Chart title visible
- [ ] Y-axis shows percentage (0-100%)

### Tab Navigation
- [ ] Click "Usage History" tab
- [ ] Usage data loads
- [ ] Model icons display
- [ ] Usage bars show properly
- [ ] Click "Accounts" tab
- [ ] Accounts grid loads
- [ ] Account cards show quota
- [ ] Click "Dashboard" tab to return

### Accounts Management
- [ ] Hover over account cards
- [ ] Cards elevate on hover
- [ ] Mini quota bars display
- [ ] "Use" button clickable
- [ ] "Delete" button clickable (don't actually delete)

### Notifications
- [ ] Toggle theme - see toast notification
- [ ] Enable/disable auto-refresh - see toast
- [ ] Toast auto-dismisses after 3 seconds
- [ ] Toast has emoji icon

---

## 📱 Mobile Testing

### Responsive Layout
- [ ] Open on mobile browser or resize window < 768px
- [ ] Stats grid shows 2 columns (not 4)
- [ ] Tabs scroll horizontally
- [ ] Theme toggle works
- [ ] Auto-refresh control stacks properly
- [ ] Chart height adjusts to 250px
- [ ] Quota cards stack in 1 column
- [ ] Account cards stack in 1 column

### Touch Interactions
- [ ] Tap theme toggle button
- [ ] Tap auto-refresh checkbox
- [ ] Tap refresh button
- [ ] Swipe tabs horizontally
- [ ] All taps respond smoothly

### Mobile Performance
- [ ] Page loads within 2 seconds
- [ ] No layout shift on load
- [ ] Scrolling is smooth
- [ ] Chart renders without lag

---

## 🎨 Visual Testing

### Dark Theme
- [ ] Background gradient visible
- [ ] Text is readable (high contrast)
- [ ] Cards have subtle borders
- [ ] Shadows are appropriate
- [ ] Chart grid lines visible

### Light Theme
- [ ] Background is light gray
- [ ] Text is dark (good contrast)
- [ ] Cards have shadows
- [ ] All elements visible
- [ ] Chart adapts to light theme

### Typography
- [ ] Inter font loaded
- [ ] All text sizes appropriate
- [ ] Headers bold and clear
- [ ] Labels readable

### Colors
- [ ] Quota bars show green/yellow/red
- [ ] Provider icons have correct colors
- [ ] Status badges colored appropriately
- [ ] Gradient buttons look good

---

## ⚡ Performance Testing

### Load Time
- [ ] Page loads < 2 seconds (good connection)
- [ ] Chart.js loads from CDN
- [ ] No console errors

### Interactions
- [ ] Theme toggle < 100ms
- [ ] Chart updates smoothly
- [ ] No lag when refreshing data
- [ ] Auto-refresh doesn't block UI

### Memory
- [ ] No memory leaks (check DevTools)
- [ ] Auto-refresh doesn't accumulate timers
- [ ] Chart updates don't leak memory

---

## 🔧 Browser Compatibility

Test in multiple browsers:
- [ ] Chrome/Edge (latest)
- [ ] Firefox (latest)
- [ ] Safari (latest)
- [ ] Mobile Safari (iOS)
- [ ] Chrome Mobile (Android)

---

## 🐛 Error Handling

### Network Errors
- [ ] Disconnect internet
- [ ] Try to refresh
- [ ] Error toast appears
- [ ] Reconnect internet
- [ ] Refresh works again

### API Errors
- [ ] Stop server
- [ ] Try to refresh
- [ ] Error message shown
- [ ] Start server
- [ ] Refresh works

---

## ✅ Final Verification

- [ ] All 6 new features working
- [ ] No console errors
- [ ] No broken images
- [ ] All links work
- [ ] Responsive on all sizes
- [ ] Theme persists
- [ ] Auto-refresh reliable

---

## 📝 Notes

**If any test fails:**
1. Check browser console for errors
2. Verify server is running
3. Clear browser cache
4. Try incognito/private mode
5. Check DASHBOARD_V2_FEATURES.md for details

**All tests passed?**
🎉 Dashboard v2 is ready for production!

---

**Testing Date**: _____________  
**Tested By**: _____________  
**Browser**: _____________  
**Result**: ⬜ Pass  ⬜ Fail
