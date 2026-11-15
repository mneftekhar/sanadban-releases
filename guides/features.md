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

# سندبان چه می‌کند

سندبان یک برنامهٔ تازه و مستقل برای ویندوز است که با رابط گرافیکیِ نو و طراحی از پایه ساخته شده است. این برنامه رایانه‌های دفاتر اسناد رسمی را از طریق سرورهای VPN سازمان به شبکهٔ سازمان وصل می‌کند تا دسترسی به سازمان امن‌تر و ساده‌تر شود.

### اتصال با یک دکمه

برای اتصال به هر سرور، همان پروتکلی استفاده می‌شود که آن سرور می‌پذیرد: SSTP، PPTP، L2TP/IPsec یا IKEv2. همهٔ این پروتکل‌ها از خودِ ویندوز هستند و برنامهٔ اضافه‌ای لازم نیست.

### فقط ترافیک سازمان از VPN

فقط ترافیک مربوط به سازمان از VPN عبور می‌کند و بقیهٔ اینترنتِ دفترخانه مستقیم است؛ این همان تفکیک ترافیک یا Split tunnel است. نام‌های سازمان هم هنگام اتصال از طریق DNS سازمان به نشانی IP تبدیل می‌شوند.

### اتصالی که برقرار می‌ماند

سندبان اتصال را مرتب بررسی می‌کند و اگر قطع شد، دوباره وصل می‌شود؛ فاصلهٔ تلاش‌ها هم هر بار کمی بیشتر می‌شود. اگر «قطع ایمن اینترنت» روشن باشد، ترافیک سازمان تا برقراری دوبارهٔ VPN از مسیر دیگری خارج نمی‌شود.

### رمز عبور در امان

نام کاربری و رمز عبور با کلید همین رایانه رمزگذاری می‌شوند و فقط سرویس سندبان از آن‌ها استفاده می‌کند. می‌توانید برای همهٔ سرورها یک اطلاعات ورود داشته باشید.

### علت را پیدا می‌کند

«عیب‌یابی» آداپتورهای شبکه، DNS، سرورها، اینترنت و VPN را بررسی می‌کند و برای کمک به حل مشکل گزارش می‌سازد. «راهنما» هم خطاهای رایج VPN ویندوز (۶۰۲، ۶۹۱، ۸۰۰، ۸۰۹، ۸۶۸) را یکی‌یکی توضیح می‌دهد.

### دسترسی مدیر، فقط یک بار

سرویس پس‌زمینه فقط یک بار نصب می‌شود. بعد از آن می‌توانید پنجره را ببندید؛ اتصال از ناحیهٔ اعلان کنار ساعت فعال می‌ماند.

### به‌روزرسانی خودکار و امضاشده

نسخهٔ جدید در پس‌زمینه و بدون مزاحمت از GitHub دریافت می‌شود. سندبان امضای توسعه‌دهنده را بررسی می‌کند و به‌روزرسانی را هنگام بی‌کاری نصب می‌کند. اگر نسخهٔ جدید درست اجرا نشود، نسخهٔ قبلی برگردانده می‌شود.

### فارسی و انگلیسی

رابط برنامه کاملاً فارسی و راست‌به‌چپ یا انگلیسی است و پوستهٔ روشن یا تیره را از ویندوز دنبال می‌کند.

## تفکیک ترافیک، به زبان ساده

فقط ترافیک مربوط به سازمان ثبت از VPN عبور می‌کند؛ بقیهٔ ترافیک دفترخانه مستقیم از اینترنت خودتان می‌رود. اگر بخواهید می‌توانید شبکه‌ها یا وب‌سایت‌های دیگری به VPN اضافه کنید یا همهٔ ترافیک را از آن عبور دهید.

<a href="#english">English ↓</a>

</div>

---

<a id="english"></a>

# What SanadBan does

SanadBan is a new, independent Windows application designed from scratch with a graphical interface, giving notary offices a safer and simpler way to connect to the registry network through its VPN servers.

### One press to connect

Each server gets the protocol it accepts: SSTP, PPTP, L2TP/IPsec or IKEv2, all built into Windows, with nothing extra to install.

### Only registry traffic through the VPN

The office internet stays as it was; only the registry network goes through the VPN (split tunnel), and registry names are looked up on the registry DNS while connected.

### A connection that stays up

The connection is checked regularly and SanadBan reconnects when it drops, waiting a little longer each time. If you want, the kill switch holds registry traffic back until the VPN is up again.

### Passwords kept safe

Logins are encrypted with this computer's key and used only by the SanadBan service. One login can serve every server.

### Finds the cause

Troubleshoot tests the network adapters, DNS, servers, internet and the VPN, and saves a report for support. The Guide explains the common Windows VPN errors (602, 691, 800, 809, 868) one by one.

### Administrator rights, once

The background service is installed once. After that you can close the window; the connection stays up from the notification area next to the clock.

### Updates itself, signed

New versions download quietly from GitHub, the developer's signature is checked, and they install while the computer is idle. If one does not start properly, the previous version comes back.

### Persian and English

Fully right-to-left Persian or English, with light and dark themes that follow Windows.

## Split tunnel, simply

Only what belongs to the registry goes through the VPN; everything else the office does keeps the speed of its own internet. You can add networks and websites of your own, or send everything through the VPN.
