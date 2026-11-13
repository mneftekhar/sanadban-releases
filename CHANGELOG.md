# Changelog / تاریخچهٔ تغییرات

Every published version of SanadBan. Installed copies update themselves; the newest download is on the
[releases page](https://github.com/mneftekhar/sanadban-releases/releases/latest).

<div dir="rtl">

همهٔ نسخه‌های منتشرشدهٔ سندبان. نسخه‌های نصب‌شده خودشان به‌روز می‌شوند؛ تازه‌ترین فایل در
[صفحهٔ انتشارها](https://github.com/mneftekhar/sanadban-releases/releases/latest) است.

</div>

---

## [0.2.1](https://github.com/mneftekhar/sanadban-releases/releases/tag/v0.2.1) — 2026-11-12 (Dodo)

One download for every Windows PC, and safer automatic updates.

### Added

- One download for every Windows PC: SanadBan-0.2.1-win.zip starts the right program for an x64 or an ARM64 processor by itself.
- Update watchdog: if a new version's background service cannot start, the previous version is put back by itself and the failed version is never offered to that PC again.

### Changed

- An update now installs early only after 30 quiet minutes: not connected, not trying to reconnect, and no window open. Otherwise it waits for the next restart.
- Restoring the previous version is done by one part at a time, so two restores can never run together.

### Fixed

- An update could install while SanadBan was waiting between automatic reconnect attempts.
- A half-finished restore left behind by an interrupted update is now set aside safely instead of blocking later updates.

### Removed

- Separate first-install downloads per processor. The per-processor files stay in each release for the automatic updates only.

<div dir="rtl">

### نسخهٔ ۰.۲.۱ (دودو)

یک فایل برای همهٔ رایانه‌های ویندوزی و به‌روزرسانی خودکارِ مطمئن‌تر.

#### افزوده شد

- یک فایل برای همهٔ رایانه‌های ویندوزی: SanadBan-0.2.1-win.zip خودش برنامهٔ مناسبِ پردازندهٔ x64 یا ARM64 را اجرا می‌کند.
- نگهبانِ به‌روزرسانی: اگر سرویس پس‌زمینهٔ نسخهٔ جدید راه نیفتد، نسخهٔ قبلی خودبه‌خود برگردانده می‌شود و آن نسخه دیگر به آن رایانه پیشنهاد نمی‌شود.

#### تغییر کرد

- به‌روزرسانی فقط پس از ۳۰ دقیقه بی‌کاری زودتر نصب می‌شود: وصل نباشد، در حال اتصال دوباره نباشد و پنجره‌ای باز نباشد. در غیر این صورت تا راه‌اندازی بعدی صبر می‌کند.
- بازگردانی نسخهٔ قبلی هر بار فقط به دست یک بخش انجام می‌شود، تا هرگز دو بازگردانی هم‌زمان رخ ندهد.

#### رفع شد

- به‌روزرسانی ممکن بود در فاصلهٔ میان تلاش‌های اتصال دوبارهٔ خودکار نصب شود.
- بازگردانیِ نیمه‌کاره‌ای که از یک به‌روزرسانیِ قطع‌شده مانده، اکنون با اطمینان کنار گذاشته می‌شود و جلوی به‌روزرسانی‌های بعدی را نمی‌گیرد.

#### حذف شد

- فایل‌های جداگانهٔ نخستین نصب برای هر پردازنده. فایل‌های جداگانه فقط برای به‌روزرسانی خودکار در هر انتشار می‌مانند.

</div>

---

## [0.1.1](https://github.com/mneftekhar/sanadban-releases/releases/tag/v0.1.1) — 2026-11-11 (Dodo)

First version delivered by the automatic updater.

### Changed

- Installed copies of 0.1.0 updated themselves to this version without anyone touching them.

### Fixed

- Releases can be built on a PC that cannot reach the .NET package server.

<div dir="rtl">

### نسخهٔ ۰.۱.۱ (دودو)

نخستین نسخه‌ای که با به‌روزرسانی خودکار رسید.

#### تغییر کرد

- نسخه‌های نصب‌شدهٔ ۰.۱.۰ بدون دخالت کسی خودشان به این نسخه به‌روز شدند.

#### رفع شد

- ساختِ نسخه روی رایانه‌ای که به سرور بسته‌های ‎.NET‎ دسترسی ندارد هم ممکن شد.

</div>

---

## [0.1.0](https://github.com/mneftekhar/sanadban-releases/releases/tag/v0.1.0) — 2026-11-11 (Dodo)

First signed release. SanadBan replaces the separate Windows VPN entries and the SsarSplitTunnel scripts.

### Added

- One window to connect, with the protocol each server accepts (SSTP, PPTP, L2TP/IPsec or IKEv2, all built into Windows).
- Split tunnel: only the registry's networks go through the VPN; registry names are looked up on the registry DNS while connected.
- Keep-alive checks, automatic reconnect, an optional kill switch, and IPv6 blocked while connected unless you allow it.
- Logins encrypted with the computer's key: one Default login for all servers, or one per server.
- Troubleshoot page that tests adapters, DNS, servers, internet and the VPN, and saves a report for support.
- Background service: administrator rights are needed once; the connection keeps going when the window is closed.
- Silent automatic updates from this page, each one signed and checked before it is installed.
- Persian and English, light and dark, and a Guide that explains every page and the common Windows VPN errors (602, 691, 800, 809, 868).

### Changed

- The app formerly called Notary VPN Client is now SanadBan. Servers, logins and settings of an existing install are carried over.
- Every system message box was replaced by the app's own confirmation window, in the app's language and theme.

### Fixed

- The service no longer runs a request with the rights of the person who sent it.
- A window crash at start, requests that could wait forever, and errors that closed the window without a trace.

### Removed

- The old Notary VPN Client service: installing SanadBan removes it and its leftover DNS rules.

<div dir="rtl">

### نسخهٔ ۰.۱.۰ (دودو)

نخستین نسخهٔ امضاشده. سندبان جای اتصال‌های جداگانهٔ VPN ویندوز و اسکریپت‌های SsarSplitTunnel را می‌گیرد.

#### افزوده شد

- یک پنجره برای اتصال، با پروتکلی که هر سرور می‌پذیرد (SSTP، PPTP، L2TP/IPsec یا IKEv2، همه از خودِ ویندوز).
- تفکیک ترافیک: فقط شبکه‌های سازمان ثبت از VPN عبور می‌کنند و نشانی‌های سازمان هنگام اتصال از DNS سازمان پرسیده می‌شوند.
- بررسیِ زنده بودن اتصال، اتصال دوبارهٔ خودکار، قطع ایمن اینترنت (اختیاری) و مسدود شدن IPv6 هنگام اتصال، مگر اینکه اجازه دهید.
- اطلاعات ورودِ رمزگذاری‌شده با کلید رایانه: یک اطلاعات ورودِ پیش‌فرض برای همهٔ سرورها یا یکی برای هر سرور.
- صفحهٔ عیب‌یابی که آداپتورها، DNS، سرورها، اینترنت و VPN را آزمایش می‌کند و گزارشی برای پشتیبانی ذخیره می‌کند.
- سرویس پس‌زمینه: دسترسی مدیر فقط یک بار لازم است و با بستن پنجره اتصال برقرار می‌ماند.
- به‌روزرسانی خودکار و بی‌صدا از همین صفحه؛ هر نسخه امضا شده و پیش از نصب بررسی می‌شود.
- فارسی و انگلیسی، روشن و تیره، و راهنمایی که همهٔ صفحه‌ها و خطاهای رایج VPN ویندوز (۶۰۲، ۶۹۱، ۸۰۰، ۸۰۹، ۸۶۸) را توضیح می‌دهد.

#### تغییر کرد

- برنامه‌ای که پیش‌تر Notary VPN Client نام داشت اکنون سندبان است. سرورها، اطلاعات ورود و تنظیماتِ نصبِ قبلی منتقل می‌شوند.
- همهٔ پیام‌های سیستمی با پنجرهٔ تأییدِ خودِ برنامه، به زبان و پوستهٔ برنامه، جایگزین شدند.

#### رفع شد

- سرویس دیگر درخواست را با دسترسیِ فرستندهٔ آن اجرا نمی‌کند.
- بسته شدن پنجره هنگام شروع، درخواست‌هایی که ممکن بود بی‌پایان منتظر بمانند، و خطاهایی که پنجره را بی‌هیچ اثری می‌بستند.

#### حذف شد

- سرویس قدیمیِ Notary VPN Client: نصب سندبان آن را همراه قانون‌های DNSِ باقی‌مانده‌اش حذف می‌کند.

</div>
