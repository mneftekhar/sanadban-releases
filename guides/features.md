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

سندبان برنامه‌ای برای ویندوز است که رایانه‌های دفاتر اسناد رسمی را از راه سرورهای VPN سازمان ثبت اسناد و املاک به شبکهٔ سازمان وصل می‌کند. جای اتصال‌های جداگانهٔ VPN ویندوز و اسکریپت‌های SsarSplitTunnel را می‌گیرد.

### یک دکمه برای اتصال

برای هر سرور همان پروتکلی به‌کار می‌رود که آن سرور می‌پذیرد: SSTP، PPTP، L2TP/IPsec یا IKEv2؛ همه از خودِ ویندوز، بدون برنامهٔ اضافه.

### فقط ترافیک سازمان از VPN

اینترنتِ دفترخانه همان‌طور که بود می‌ماند و فقط شبکهٔ سازمان ثبت از VPN عبور می‌کند (تفکیک ترافیک یا Split tunnel). نشانی‌های سازمان هنگام اتصال از DNS سازمان پرسیده می‌شوند.

### اتصالی که برقرار می‌ماند

زنده بودنِ اتصال مرتب بررسی می‌شود و اگر قطع شود، سندبان دوباره وصل می‌شود و هر بار کمی بیشتر صبر می‌کند. «قطع ایمن اینترنت» هم اگر بخواهید، ترافیک سازمان را تا برگشتنِ VPN نگه می‌دارد.

### رمز عبور در امان

اطلاعات ورود با کلید همین رایانه رمزگذاری می‌شود و فقط سرویس سندبان از آن استفاده می‌کند. یک اطلاعات ورود برای همهٔ سرورها کافی است.

### علت را پیدا می‌کند

«عیب‌یابی» آداپتورهای شبکه، DNS، سرورها، اینترنت و VPN را آزمایش می‌کند و گزارشی برای پشتیبانی می‌سازد. «راهنما» خطاهای رایج VPN ویندوز (۶۰۲، ۶۹۱، ۸۰۰، ۸۰۹، ۸۶۸) را یکی‌یکی توضیح می‌دهد.

### دسترسی مدیر، فقط یک بار

سرویس پس‌زمینه یک بار نصب می‌شود. پس از آن می‌توانید پنجره را ببندید؛ اتصال از ناحیهٔ اعلان کنار ساعت برقرار می‌ماند.

### خودش به‌روز می‌شود، با امضا

نسخهٔ جدید بی‌صدا از GitHub دریافت می‌شود، امضای توسعه‌دهنده بررسی می‌شود و وقتی رایانه بی‌کار است نصب می‌شود. اگر درست راه نیفتد، نسخهٔ قبلی برمی‌گردد.

### فارسی و انگلیسی

فارسیِ کاملاً راست‌به‌چپ یا انگلیسی، با پوستهٔ روشن و تیره که از ویندوز پیروی می‌کند.

## تفکیک ترافیک، به زبان ساده

فقط آنچه به سازمان ثبت مربوط است از VPN می‌رود؛ باقیِ کارهای دفترخانه سرعتِ اینترنتِ خودش را دارد. اگر بخواهید، شبکه‌ها و وب‌سایت‌های دیگری هم اضافه کنید یا همه‌چیز را از VPN بفرستید.

<a href="#english">English ↓</a>

</div>

---

<a id="english"></a>

# What SanadBan does

SanadBan is a Windows app that connects the computers of Iranian notary offices to the registry network through the registry's VPN servers. It replaces the separate Windows VPN entries and the SsarSplitTunnel scripts.

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
