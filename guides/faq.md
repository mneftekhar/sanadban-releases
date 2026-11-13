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

# پرسش‌های رایج

### سندبان چیست و برای چه کسانی است؟

برنامه‌ای برای ویندوز که رایانه‌های دفاتر اسناد رسمی (دفترخانه‌ها) را از راه VPN به شبکهٔ سازمان ثبت اسناد و املاک وصل می‌کند؛ برای سردفتران، دفتریاران، کارکنان دفترخانه و پشتیبان‌های فنی آن‌ها.

### آیا سندبان محصول سازمان ثبت است؟

خیر. سندبان را م. افتخار به‌صورت مستقل ساخته است و ساخته یا وابسته به سازمان ثبت اسناد و املاک کشور نیست. نام کاربری و رمز عبور VPN را همچنان سازمان به دفترخانه می‌دهد.

### با کدام ویندوز کار می‌کند؟

ویندوز ۱۰ و ۱۱، روی رایانه‌های x64 (اینتل و AMD) و ARM64، با یک فایلِ مشترک. ‎.NET 10 Desktop Runtime‎ مایکروسافت هم باید نصب باشد.

### از کدام پروتکل‌های VPN پشتیبانی می‌کند؟

SSTP، PPTP، L2TP/IPsec و IKEv2؛ همان پروتکل‌هایی که خودِ ویندوز دارد. برای هر سرور همان پروتکلی به‌کار می‌رود که آن سرور می‌پذیرد.

### آیا جای اسکریپت SsarSplitTunnel را می‌گیرد؟

بله؛ سندبان جای آن اسکریپت‌ها و اتصال‌های جداگانهٔ VPN ویندوز را می‌گیرد. گامی که رایانه‌ای را که پیش‌تر اسکریپت داشته به‌طور تمیز تحویل بگیرد در نقشهٔ راه است.

### رمز عبور من کجا نگه داشته می‌شود؟

روی همان رایانه، رمزگذاری‌شده با کلیدِ رایانه، و فقط سرویس سندبان از آن استفاده می‌کند. جز به سرور VPN هنگام اتصال، به هیچ جا فرستاده نمی‌شود.

### سندبان چطور به‌روز می‌شود؟

خودکار و بی‌صدا. سرویس پس‌زمینه نسخهٔ جدید را از همین صفحهٔ GitHub دریافت می‌کند، امضای توسعه‌دهنده را بررسی می‌کند و هنگام بی‌کاری یا راه‌اندازی دوباره نصب می‌کند؛ هرگز در میانهٔ اتصال.

### نسخهٔ لینوکس دارد؟

هنوز نه. پس از آزمایشِ کاملِ نسخهٔ ویندوز، نسخهٔ لینوکس با همین طراحی برای Ubuntu، Mint و Arch ساخته می‌شود.

<a href="#english">English ↓</a>

</div>

---

<a id="english"></a>

# Frequently asked questions

### What is SanadBan, and who is it for?

A Windows app that connects the computers of Iranian notary offices to the network of the Registration Organization of Deeds and Properties over VPN; for notaries, their staff and the people who support them.

### Is SanadBan made by the registry?

No. SanadBan is an independent project by M. Eftekhar and is not made by or affiliated with the Registration Organization. The VPN user name and password still come from the registry.

### Which Windows does it run on?

Windows 10 and 11, on x64 (Intel and AMD) and ARM64 computers, from one shared file. Microsoft's .NET 10 Desktop Runtime must be installed too.

### Which VPN protocols does it support?

SSTP, PPTP, L2TP/IPsec and IKEv2, the protocols built into Windows. Each server is used with the protocol it accepts.

### Does it replace the SsarSplitTunnel script?

Yes; SanadBan replaces those scripts and the separate Windows VPN entries. A step that cleanly takes over a computer that ran the script is on the roadmap.

### Where is my password kept?

On that computer, encrypted with the computer's key, and used only by the SanadBan service. It is never sent anywhere except to the VPN server while connecting.

### How does SanadBan update?

Automatically and quietly. The background service downloads new versions from this GitHub page, checks the developer's signature and installs while idle or at the next restart, never during a connection.

### Is there a Linux version?

Not yet. Once the Windows version is fully tested, a Linux version with the same design will follow for Ubuntu, Mint and Arch.
