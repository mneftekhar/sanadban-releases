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

# رفع مشکل‌های رایج

همین توضیح‌ها در صفحهٔ «راهنما»ی خودِ برنامه هم هست. اگر چیزی کار نکرد، «عیب‌یابی» را اجرا کنید و «ذخیره برای پشتیبانی» را بزنید.

### گیر کردن روی «در حال برقراری ارتباط با سرور» یا خطای ۸۰۰ ویندوز

سرور پاسخ نمی‌دهد. معمولاً خاموش است، خارج از زمانِ در دسترس بودنش است، در این شبکه مسدود است یا روی پروتکلی تنظیم شده که نمی‌پذیرد. «عیب‌یابی» را اجرا کنید: بخش «سرورها» نشان می‌دهد کدام درگاه‌ها پاسخ می‌دهند.

### خطای ۶۹۱ (نام کاربری یا رمز عبور)

نام کاربری یا رمز عبور پذیرفته نشد. آن‌ها را در صفحهٔ «اطلاعات ورود» بررسی کنید («تغییر» را بزنید و رمز را دوباره وارد کنید). اگر درست است، ممکن است حساب قفل یا منقضی شده باشد؛ از سازمان بپرسید.

### خطای ۸۰۹

شبکهٔ میان این رایانه و سرور، اتصال را مسدود کرد. در PPTP و L2TP/IPsec پشت برخی مودم‌ها و ارائه‌دهندگان اینترنت رایج است؛ معمولاً سرورِ SSTP کار می‌کند.

### خطای ۸۶۸

نام سرور پیدا نشد. اتصال اینترنت را بررسی و «عیب‌یابی» را اجرا کنید؛ بخش DNS نشان می‌دهد کدام سرور DNS پاسخ نمی‌دهد.

### خطای ۶۰۲

ویندوز گمان می‌کند یک درگاهِ اتصال از قبل باز است؛ معمولاً پس از اتصالی که درست بسته نشده. راه‌اندازی دوبارهٔ رایانه آن را برطرف می‌کند.

### «برای این سرور نام کاربری و رمز عبوری ذخیره نشده است»

در صفحهٔ «اطلاعات ورود»، برای همهٔ سرورها یا همان سرور، اطلاعات ورود اضافه کنید.

### اتصال پس از مدتی بی‌کاری قطع می‌شود

مطمئن شوید «زنده نگه‌داشتن اتصال» روشن است (صفحهٔ «تفکیک ترافیک») و نشانی آن پاسخ می‌دهد («عیب‌یابی»، بخش «اتصال VPN»).

### سایت‌های سازمان با نامشان باز نمی‌شوند

وصل شوید و «عیب‌یابی» را اجرا کنید: بخش «اتصال VPN» نشان می‌دهد قانون DNS سازمان فعال است یا نه.

### پس از قطع VPN، اینترنت از کار افتاد

این کارِ «قطع ایمن اینترنت» برای محافظت از شماست. دوباره وصل شوید یا در صفحهٔ «خانه»، «اینترنت را تا اتصال بعدی آزاد کن» را بزنید.

<a href="#english">English ↓</a>

</div>

---

<a id="english"></a>

# Common problems

The same answers are in the app's own Guide page. If something does not work, run Troubleshoot and press Save for support.

### Stuck on "Contacting the server", or Windows error 800

The server does not answer. Usually it is switched off, outside the hours it is available, blocked on this network, or set to a protocol it does not accept. Run Troubleshoot: the Servers section shows which ports answer.

### Error 691 (user name or password)

The user name or password was not accepted. Check them on Logins (press Change and type the password again). If they are right, the account may be locked or expired; ask the registry.

### Error 809

The network between this computer and the server blocked the connection. Common with PPTP and L2TP/IPsec behind some routers and internet providers; an SSTP server usually works.

### Error 868

The server's name could not be found. Check the internet connection and run Troubleshoot; the DNS section shows which DNS server fails.

### Error 602

Windows thinks a connection port is already open, usually after an earlier connection did not close cleanly. Restarting the computer clears it.

### "No user name and password are saved for this server"

Add a login on Logins, for all servers or for that server.

### The connection drops after a while with no activity

Make sure Keep the connection alive is on (Split tunnel page) and its address answers (Troubleshoot, VPN connection section).

### Registry websites do not open by name

Connect, then run Troubleshoot: the VPN connection section shows whether the registry DNS rule is active.

### The internet stopped working after the VPN dropped

That is the kill switch protecting you. Connect again, or press Allow internet until the next connection on Home.
