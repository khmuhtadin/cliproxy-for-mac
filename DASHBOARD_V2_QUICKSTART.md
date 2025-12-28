# 🚀 Dashboard v2 - Quick Start Guide

## ⚡ Instant Access

### 1. Start Server (if not running)
```bash
cd /Users/khmuhtadin/.cli-proxy-api
./run-server.sh
```

### 2. Open Dashboard v2
```
http://localhost:8317/dashboard-v2.html
```

That's it! 🎉

---

## 🎯 Quick Feature Tour

### Theme Toggle (Top Right)
Click **🌓** to switch between dark/light mode

### Auto-Refresh Control (Dashboard Tab)
- **✅ Checked** = Auto-refresh every 30s
- **Countdown** shows next refresh time
- **Manual refresh** button still available

### Interactive Chart
Scroll down in Dashboard tab to see quota visualization

### Mobile View
Open on your phone - fully optimized!

---

## 🔄 Comparison

| URL | Version | Features |
|-----|---------|----------|
| `/dashboard.html` | v1 (Original) | Basic, Dark only |
| `/dashboard-v2.html` | v2 (Enhanced) | ✅ All new features |

---

## 🎨 Try This

1. **Toggle theme** - Click 🌓 and watch everything change
2. **Disable auto-refresh** - Uncheck the Auto checkbox
3. **Watch the chart** - See quota distribution visually
4. **Resize window** - Notice responsive design

---

## 📱 Mobile Test

Open on your phone:
```
http://[YOUR_IP]:8317/dashboard-v2.html
```

---

## ⚙️ Optional: Make v2 Default

Replace original dashboard:
```bash
cd /Users/khmuhtadin/.cli-proxy-api/static
cp dashboard-v2.html dashboard.html
```

Now `http://localhost:8317/dashboard.html` uses v2!

---

## 📚 Full Documentation

See `DASHBOARD_V2_FEATURES.md` for complete feature list

---

**Enjoy! 🚀**
