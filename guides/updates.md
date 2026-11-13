<!-- This page is generated from site/content.json; edit that file, not this one. -->
<p align="center">
  <a href="../README.md">خانه · Home</a> &nbsp;|&nbsp;
  <a href="features.md">امکانات · Features</a> &nbsp;|&nbsp;
  <a href="screenshots.md">تصویرها · Screenshots</a> &nbsp;|&nbsp;
  <a href="install.md">نصب · Install</a> &nbsp;|&nbsp;
  <a href="troubleshooting.md">رفع مشکل · Troubleshooting</a> &nbsp;|&nbsp;
  <a href="faq.md">پرسش‌ها · FAQ</a> &nbsp;|&nbsp;
  <a href="roadmap.md">نقشهٔ راه · Roadmap</a> &nbsp;|&nbsp;
  <a href="updates.md">به‌روزرسانی · Updates</a> &nbsp;|&nbsp;
  <a href="privacy.md">حریم خصوصی · Privacy</a> &nbsp;|&nbsp;
  <a href="../CHANGELOG.md">تغییرات · Changelog</a> &nbsp;|&nbsp;
  <a href="https://mneftekhar.github.io/sanadban-releases/">وب‌سایت · Website</a>
</p>

<div dir="rtl">

# به‌روزرسانی و امنیت

- سرویس پس‌زمینه چند دقیقه پس از روشن شدنِ ویندوز و سپس هر چند ساعت یک بار وجود نسخهٔ جدید را بررسی می‌کند.
- هر رایانه فقط به‌روزرسانیِ مخصوص پردازندهٔ خودش (x64 یا ARM64) را دریافت می‌کند. فایلِ واحدِ `SanadBan-<نسخه>-win.zip` فقط برای نخستین نصب است.
- پیش از هر استفاده، سندبان بررسی می‌کند که نسخه با کلید خصوصیِ توسعه‌دهنده امضا شده باشد و همهٔ فایل‌ها دقیقاً همان فایل‌های امضاشده باشند. فایلی که رد شود پاک می‌شود و هرگز اجرا نمی‌شود.
- نسخهٔ جدید در راه‌اندازیِ بعدیِ سرویس نصب می‌شود، یا زودتر وقتی سندبان ۳۰ دقیقه استفاده نشده باشد؛ هرگز در میانهٔ اتصال یا اتصال دوبارهٔ خودکار. اگر درست شروع به کار نکند، نسخهٔ قبلی خودکار برگردانده می‌شود.

<a href="#english">English ↓</a>

</div>

---

<a id="english"></a>

# Updates and security

- The background service checks for a new version a few minutes after Windows starts and then every few hours.
- Each computer downloads only the update made for its own processor (x64 or ARM64). The one file `SanadBan-<version>-win.zip` is only for the first install.
- Before anything is used, SanadBan checks that the version was signed with the developer's private key and that every file is exactly the one that was signed. A file that fails is deleted and never run.
- The new version installs the next time the service starts, or earlier once SanadBan has not been used for 30 minutes; never during a connection or an automatic reconnect. If it does not start correctly, the previous version is put back automatically.
