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

این پاسخ‌ها همان توضیح‌های صفحهٔ «راهنما»ی برنامه‌اند. اگر مشکلی داشتید، «عیب‌یابی» را اجرا کنید و «ذخیره برای پشتیبانی» را بزنید تا گزارش ساخته شود.

### گیر کردن روی «در حال برقراری ارتباط با سرور» یا خطای ۸۰۰ ویندوز

سرور پاسخ نمی‌دهد. معمولاً یکی از این علت‌هاست: سرور خاموش یا خارج از ساعات در دسترس است، شبکهٔ شما اتصال را مسدود می‌کند یا پروتکل انتخاب‌شده با سرور سازگار نیست. «عیب‌یابی» را اجرا کنید؛ در بخش «سرورها» می‌بینید کدام درگاه‌ها پاسخ می‌دهند.

### خطای ۶۹۱ (نام کاربری یا رمز عبور)

نام کاربری یا رمز عبور پذیرفته نشده است. در «اطلاعات ورود» آن‌ها را بررسی کنید و رمز را دوباره وارد کنید. اگر مطمئن هستید که درست‌اند، ممکن است حساب قفل یا منقضی شده باشد؛ در این صورت با سازمان تماس بگیرید.

### خطای ۸۰۹

ارتباط میان رایانه و سرور در شبکه قطع یا مسدود می‌شود. این مشکل بیشتر در PPTP و L2TP/IPsec و پشت بعضی مودم‌ها یا سرویس‌دهنده‌های اینترنت دیده می‌شود. معمولاً SSTP راه حل بهتری است.

### خطای ۸۶۸

نام سرور پیدا نمی‌شود. ابتدا اتصال اینترنت را بررسی کنید و سپس «عیب‌یابی» را اجرا کنید؛ بخش DNS نشان می‌دهد کدام سرور DNS نمی‌تواند نام را به نشانی IP برساند.

### خطای ۶۰۲

ویندوز تصور می‌کند درگاه اتصال هنوز از اتصال قبلی باز مانده است. این معمولاً وقتی اتصال قبلی درست بسته نشده رخ می‌دهد. برای پاک شدن این حالت، رایانه را دوباره راه‌اندازی کنید.

### «برای این سرور نام کاربری و رمز عبوری ذخیره نشده است»

در «اطلاعات ورود» یک ورود جدید برای همهٔ سرورها یا فقط همان سرور اضافه کنید.

### اتصال پس از مدتی بی‌کاری قطع می‌شود

مطمئن شوید «زنده نگه‌داشتن اتصال» در صفحهٔ «تفکیک ترافیک» روشن است. این ویژگی برای حفظ اتصال، به نشانی مشخص‌شده ترافیک دوره‌ای می‌فرستد. اگر ping پاسخی نداشت، ممکن است شبکه یا سرور ICMP را مسدود کرده باشد؛ این به‌تنهایی نشانهٔ خرابی نیست. به‌جای تکیه بر ping، باز شدن سایت‌های سازمان و پایدار ماندن اتصال را بررسی کنید.

### سایت‌های سازمان با نامشان باز نمی‌شوند

ابتدا به VPN وصل شوید و «عیب‌یابی» را اجرا کنید. در بخش «اتصال VPN» می‌بینید قانون DNS سازمان فعال است یا نه.

### بعد از قطع شدن VPN، ترافیکی که باید از آن عبور می‌کرد مسدود شده است

این همان کار «قطع ایمن اینترنت» است. در حالت تفکیک ترافیک فقط ترافیک سازمان مسدود می‌شود و بقیهٔ اینترنت کار خود را ادامه می‌دهد. اگر همهٔ ترافیک از VPN برود، کل اینترنت مسدود می‌شود. برای برطرف کردن آن، دوباره وصل شوید یا در «خانه» روی «عبور ترافیک بیرون از VPN را تا اتصال بعدی آزاد کن» بزنید.

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

Make sure Keep the connection alive is on (Split tunnel page). It sends periodic traffic; an unanswered ping may be blocked even while the connection stays active. Check registry reachability and connection stability, not ping alone.

### Registry websites do not open by name

Connect, then run Troubleshoot: the VPN connection section shows whether the registry DNS rule is active.

### Traffic meant for the VPN is blocked after a drop

That is the kill switch protecting you. In split tunnel, only registry traffic is blocked and ordinary internet continues; in full tunnel, the internet is blocked. Connect again, or press Allow traffic outside the VPN until the next connection on Home.
