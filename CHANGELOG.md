<!-- This page is generated from site/content.json; edit that file, not this one. -->
<p align="center">
  <a href="README.md">خانه · Home</a> &nbsp;|&nbsp;
  <a href="guides/features.md">امکانات · Features</a> &nbsp;|&nbsp;
  <a href="guides/screenshots.md">تصویرها · Screenshots</a> &nbsp;|&nbsp;
  <a href="guides/install.md">نصب · Install</a> &nbsp;|&nbsp;
  <a href="guides/troubleshooting.md">رفع مشکل · Troubleshooting</a> &nbsp;|&nbsp;
  <a href="guides/faq.md">پرسش‌ها · FAQ</a> &nbsp;|&nbsp;
  <a href="guides/roadmap.md">نقشهٔ راه · Roadmap</a> &nbsp;|&nbsp;
  <a href="guides/updates.md">به‌روزرسانی · Updates</a> &nbsp;|&nbsp;
  <a href="guides/privacy.md">حریم خصوصی · Privacy</a> &nbsp;|&nbsp;
  <a href="CHANGELOG.md">تغییرات · Changelog</a> &nbsp;|&nbsp;
  <a href="https://mneftekhar.github.io/sanadban-releases/">وب‌سایت · Website</a>
</p>

<div dir="rtl">

# تاریخچهٔ تغییرات

همهٔ نسخه‌های منتشرشدهٔ سندبان. نسخهٔ نصب‌شده روی رایانهٔ شما به‌صورت خودکار به‌روز می‌شود.

## [۰.۲.۲](https://github.com/mneftekhar/sanadban-releases/releases/tag/v0.2.2) — ۲۴ آبان ۱۴۰۵

ساخت آزمایشی آلفا. رایانه‌های واقعی x64، به‌روزرسانی نسخهٔ نصب‌شده، رابط کاربری و چند آزمایش اتصال واقعی هنوز تأیید نشده‌اند؛ SABT1 و SABT4 با PPTP در شبکهٔ آزمایش وصل نشدند. نسخهٔ پایدار 0.2.1 همچنان آخرین انتشار برای به‌روزرسانی خودکار است.

**رفع شد**

- توضیحات قطع ایمن اینترنت، زنده نگه‌داشتن اتصال و IPv6 در حالت تفکیک ترافیک، به فارسی و انگلیسی اصلاح شد.
- با قطع اتصال عمدی، اخطار قدیمیِ اتصال دوباره پاک می‌شود.

## [۰.۲.۱](https://github.com/mneftekhar/sanadban-releases/releases/tag/v0.2.1) — ۲۱ آبان ۱۴۰۵ (دودو)

یک فایل برای همهٔ رایانه‌های ویندوزی و به‌روزرسانی خودکارِ امن‌تر.

**افزوده شد**

- یک فایل برای همهٔ رایانه‌های ویندوزی: SanadBan-0.2.1-win.zip خودش نسخهٔ مناسب پردازندهٔ رایانهٔ شما (x64 یا ARM64) را اجرا می‌کند.
- نگهبانِ به‌روزرسانی: اگر سرویس پس‌زمینهٔ نسخهٔ جدید اجرا نشود، نسخهٔ قبلی به‌طور خودکار برگردانده می‌شود و نسخهٔ معیوب دیگر به آن رایانه پیشنهاد نمی‌شود.

**تغییر کرد**

- به‌روزرسانی فقط پس از ۳۰ دقیقه بی‌کاری زودتر نصب می‌شود: VPN وصل نباشد، تلاش برای اتصال دوباره در جریان نباشد و پنجرهٔ برنامه باز نباشد. در غیر این صورت تا راه‌اندازی بعدی صبر می‌کند.
- بازگردانی نسخهٔ قبلی فقط توسط یک فرایند و در یک مرحله انجام می‌شود تا دو عملیات بازگردانی هم‌زمان اجرا نشوند.

**رفع شد**

- به‌روزرسانی ممکن بود هنگام انتظار میان دو تلاش برای اتصال دوباره نصب شود.
- بازگردانی نیمه‌کاره‌ای که پس از قطع شدن به‌روزرسانی باقی مانده است، اکنون با اطمینان کنار گذاشته می‌شود و جلوی به‌روزرسانی‌های بعدی را نمی‌گیرد.

**حذف شد**

- فایل‌های جداگانهٔ نصب اولیه برای هر پردازنده حذف شدند؛ فایل‌های مخصوص هر پردازنده فقط برای به‌روزرسانی خودکار باقی می‌مانند.

## [۰.۱.۱](https://github.com/mneftekhar/sanadban-releases/releases/tag/v0.1.1) — ۲۰ آبان ۱۴۰۵ (دودو)

نخستین نسخه‌ای که با به‌روزرسانی خودکار رسید.

**تغییر کرد**

- نسخه‌های نصب‌شدهٔ ۰.۱.۰ بدون دخالت کسی خودشان به این نسخه به‌روز شدند.

**رفع شد**

- ساختِ نسخه روی رایانه‌ای که به سرور بسته‌های ‎.NET‎ دسترسی ندارد هم ممکن شد.

## [۰.۱.۰](https://github.com/mneftekhar/sanadban-releases/releases/tag/v0.1.0) — ۲۰ آبان ۱۴۰۵ (دودو)

نخستین انتشار امضاشده. سندبان برنامه‌ای تازه با رابط گرافیکی برای اتصال امن و آسان به شبکهٔ سازمان است.

**افزوده شد**

- یک پنجره برای اتصال که برای هر سرور از پروتکل پذیرفته‌شدهٔ همان سرور استفاده می‌کند: SSTP، PPTP، L2TP/IPsec یا IKEv2؛ همه از خودِ ویندوز.
- تفکیک ترافیک: فقط شبکه‌های سازمان از VPN عبور می‌کنند و نام‌های سازمان هنگام اتصال از طریق DNS سازمان به نشانی IP تبدیل می‌شوند.
- بررسی زنده بودن اتصال، اتصال دوبارهٔ خودکار، قطع ایمن اینترنت اختیاری و مسدود شدن IPv6 هنگام اتصال، مگر اینکه اجازهٔ عبور آن را بدهید.
- اطلاعات ورود رمزگذاری‌شده با کلید رایانه: یک ورود پیش‌فرض برای همهٔ سرورها یا یک ورود جداگانه برای هر سرور.
- صفحهٔ عیب‌یابی که آداپتورها، DNS، سرورها، اینترنت و VPN را بررسی می‌کند و برای کمک به حل مشکل گزارش می‌سازد.
- سرویس پس‌زمینه: دسترسی مدیر فقط یک بار لازم است و اتصال پس از بستن پنجره نیز برقرار می‌ماند.
- به‌روزرسانی خودکار و بدون مزاحمت از همین صفحه؛ هر نسخه امضا می‌شود و پیش از نصب بررسی می‌شود.
- رابط فارسی و راست‌به‌چپ یا انگلیسی، با پوستهٔ روشن و تیره، و راهنمایی که همهٔ صفحه‌ها و خطاهای رایج VPN ویندوز (۶۰۲، ۶۹۱، ۸۰۰، ۸۰۹، ۸۶۸) را توضیح می‌دهد.

**تغییر کرد**

- نام برنامه از Notary VPN Client به SanadBan تغییر کرد. سرورها، اطلاعات ورود و تنظیمات نصب قبلی منتقل می‌شوند.
- همهٔ پیام‌های سیستمی با پنجرهٔ تأییدِ خودِ برنامه، به زبان و پوستهٔ برنامه، جایگزین شدند.

**رفع شد**

- سرویس دیگر درخواست را با دسترسیِ فرستندهٔ آن اجرا نمی‌کند.
- بسته شدن ناگهانی پنجره هنگام شروع، انتظار بی‌پایان برای برخی درخواست‌ها و بسته شدن پنجره بدون ثبت خطا رفع شد.

**حذف شد**

- سرویس قدیمی Notary VPN Client و قوانین DNS باقی‌مانده از آن هنگام نصب سندبان حذف می‌شوند.

<a href="#english">English ↓</a>

</div>

---

<a id="english"></a>

# Changelog

Every published version of SanadBan. Installed copies update themselves.

## [0.2.2](https://github.com/mneftekhar/sanadban-releases/releases/tag/v0.2.2) — 15 November 2026

Alpha test build. Real x64 PCs, installed updates, interactive UI and several live connection cases are not yet verified; SABT1/SABT4 PPTP did not connect on the tested network. Stable 0.2.1 remains the latest automatic-update release.

**Fixed**

- clarified split-tunnel kill-switch, keep-alive and IPv6 guidance in English and Persian.
- deliberate Disconnect now clears stale reconnect notices.

## [0.2.1](https://github.com/mneftekhar/sanadban-releases/releases/tag/v0.2.1) — 12 November 2026 (Dodo)

One download for every Windows PC, and safer automatic updates.

**Added**

- One download for every Windows PC: SanadBan-0.2.1-win.zip starts the right program for an x64 or an ARM64 processor by itself.
- Update watchdog: if a new version's background service cannot start, the previous version is put back by itself and the failed version is never offered to that PC again.

**Changed**

- An update now installs early only after 30 quiet minutes: not connected, not trying to reconnect, and no window open. Otherwise it waits for the next restart.
- Restoring the previous version is done by one part at a time, so two restores can never run together.

**Fixed**

- An update could install while SanadBan was waiting between automatic reconnect attempts.
- A half-finished restore left behind by an interrupted update is now set aside safely instead of blocking later updates.

**Removed**

- Separate first-install downloads per processor. The per-processor files stay in each release for the automatic updates only.

## [0.1.1](https://github.com/mneftekhar/sanadban-releases/releases/tag/v0.1.1) — 11 November 2026 (Dodo)

First version delivered by the automatic updater.

**Changed**

- Installed copies of 0.1.0 updated themselves to this version without anyone touching them.

**Fixed**

- Releases can be built on a PC that cannot reach the .NET package server.

## [0.1.0](https://github.com/mneftekhar/sanadban-releases/releases/tag/v0.1.0) — 11 November 2026 (Dodo)

First signed release. SanadBan introduces a new graphical application for secure, simple registry connections.

**Added**

- One window to connect, with the protocol each server accepts (SSTP, PPTP, L2TP/IPsec or IKEv2, all built into Windows).
- Split tunnel: only the registry's networks go through the VPN; registry names are looked up on the registry DNS while connected.
- Keep-alive checks, automatic reconnect, an optional kill switch, and IPv6 blocked while connected unless you allow it.
- Logins encrypted with the computer's key: one Default login for all servers, or one per server.
- Troubleshoot page that tests adapters, DNS, servers, internet and the VPN, and saves a report for support.
- Background service: administrator rights are needed once; the connection keeps going when the window is closed.
- Silent automatic updates from this page, each one signed and checked before it is installed.
- Persian and English, light and dark, and a Guide that explains every page and the common Windows VPN errors (602, 691, 800, 809, 868).

**Changed**

- The app formerly called Notary VPN Client is now SanadBan. Servers, logins and settings of an existing install are carried over.
- Every system message box was replaced by the app's own confirmation window, in the app's language and theme.

**Fixed**

- The service no longer runs a request with the rights of the person who sent it.
- A window crash at start, requests that could wait forever, and errors that closed the window without a trace.

**Removed**

- The old Notary VPN Client service: installing SanadBan removes it and its leftover DNS rules.
