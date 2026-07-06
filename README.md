<!--
title: Basilisk — the autonomous pentesting agent that runs on your own machine
description: Basilisk is the nervous system for a large language model — an open-source, autonomous pentesting agent that runs as a native Linux desktop app on your own hardware. The model is the brain; Basilisk gives it a full offensive toolchain, desktop and shell control, a tamper-evident evidence ledger, and a hard structural safety floor. Bring your own model (SiliconFlow, Groq). It runs on your machine and answers only to you. 51 of 113 OWASP Juice Shop challenges solved fully autonomously.
keywords: pentesting agent, ai pentest tool, autonomous pentest agent, kali linux ai, offensive security ai, llm security agent, deepseek security agent, evidence ledger, juice shop benchmark, prompt injection defense, mcp client, nethunter ai, gtk4 app, siliconflow, red team assistant, rokos basilisk
-->

<div align="center">

<img src="banner.png" alt="BASILISK — the serpent on your machine" width="820">

### The model is the brain. Basilisk is the nervous system — it lets the brain see, touch, and act.

*The autonomous pentesting agent that runs on your machine, answers only to you, and never forgets a move it made.*

<br>

![version](https://img.shields.io/badge/version-5.2.0-7d121b?style=for-the-badge&labelColor=08090b)
![license](https://img.shields.io/badge/license-MIT-7d121b?style=for-the-badge&labelColor=08090b)
![platform](https://img.shields.io/badge/Linux-X11%20%7C%20Wayland-6d7680?style=for-the-badge&logo=linux&logoColor=white&labelColor=08090b)
![python](https://img.shields.io/badge/python-3.10+-6d7680?style=for-the-badge&logo=python&logoColor=white&labelColor=08090b)

![mobile](https://img.shields.io/badge/runs%20on-NetHunter-6d7680?style=for-the-badge&labelColor=08090b)
![ledger](https://img.shields.io/badge/evidence-tamper--evident-7d121b?style=for-the-badge&labelColor=08090b)
![injection](https://img.shields.io/badge/prompt%20injection-surface%20closed-7d121b?style=for-the-badge&labelColor=08090b)
![benchmark](https://img.shields.io/badge/Juice%20Shop-51%2F113%20fully%20autonomous-7d121b?style=for-the-badge&labelColor=08090b)

</div>

<br>

---

Roko's Basilisk was a thought experiment about an AI you'd want to be on the right side of. **This one is real, it's yours, and it breaks things you're allowed to break.**

A language model can *talk* about a pentest. It can't run one — it can't see your screen, drive your tools, or prove what it did. Basilisk is the body around that brain: point it at an authorized target, turn it loose, and it runs the whole engagement on its own — recon, exploitation, the write-up — handing you a tamper-evident receipt for every command it fired. Turned loose black-box on OWASP Juice Shop, it solved **51 of 113 challenges unattended.**

**Bring your own model. Own your machine. Break what you're allowed to break.**

<br>

<div align="center">
<img src="dragon.png" alt="Basilisk" width="320">
</div>

<br>

---

## ⚡ Install — your call: trust me, or read every line

Basilisk runs shell commands on your machine **as you.** Decide how much you trust a stranger's code, then pick a path — no dark patterns.

**A — you trust me. One line:**

```bash
curl -fsSL https://raw.githubusercontent.com/the-priest/Basilisk/main/install.sh | bash
```

**B — you don't (smart). Clone it, read it, run it:**

```bash
git clone https://github.com/the-priest/Basilisk.git kali
```
```bash
cd kali
```
```bash
less install.sh
```
```bash
./install.sh
```

Plain Python and one shell script — nothing phones home, nothing hides in a binary, and the test suites are stdlib-only so you can run them before you trust it with anything. The same command updates it: it auto-detects your distro, parse-checks every file before it touches disk, and backs up your chat history. No Docker, no daemon, no account.

<br>

---

## ▶ See it in action

https://github.com/user-attachments/assets/7df7b6a9-744d-46ec-9ce6-c8ae924fc786

https://github.com/user-attachments/assets/8b633570-a7b2-4345-a5ee-41b02e5ddfc3

https://github.com/user-attachments/assets/8ab0cb29-a66d-4cfd-880b-0365a32cc3a7

<br>

---

## Why Basilisk

- **It's an operator, not a chatbot.** It runs its own commands, chains them, and finishes the job unattended — no "confirm every step," no approval cards. Turn it loose on a target and walk away.
- **It runs on your hardware.** Not a website, not someone's cloud. The only thing that ever leaves is the API call to the model provider *you* picked. Your keys, your data, your machine.
- **It proves its work.** Every command is hashed into a tamper-evident evidence ledger — a receipt you can hand a client, not a story it made up afterward.
- **It can't be turned against you.** The tools that pulled in attacker-controlled text are *gone*, what's left reads only from sources an attacker can't aim, and the one command that could wipe your box is refused at a hard floor with no override.
- **It goes where you go.** The same app on a Kali NetHunter phone as on your laptop — an operator's assistant in your pocket.

<br>

---

## What it does

Point Basilisk at an authorized target and it walks the whole engagement in one window. It inventories your installed tooling, builds an **ordered recon plan** (passive first), runs the commands autonomously **within the scope you set**, parses raw scanner output into clean findings, and **ranks CVEs by what's actually being exploited in the wild** (NVD → CISA KEV → EPSS). The moment it gets in, it writes the reproducible *"how we got in"* report straight from the evidence ledger — backed by real hashed commands, not a retelling. It builds and fires real exploits — SQLi, JWT forgery, NoSQL/XXE injection, coupon and CAPTCHA bypass, sqlmap-driven attacks — against targets you're allowed to test.

And when it hits something it doesn't know, it doesn't guess: it reads the answer from a fixed allow-list of vetted sources — NVD, MITRE, CISA and vendor advisories, plus PortSwigger, MDN, GitHub, Wikipedia, and reputable news — and cites it. It can't fetch anything off that list.

Off the offensive path, the same body does the rest of an operator's day:

- **Audit your own code & deps** — drives ten industry scanners (Semgrep, Bandit, gitleaks, OSV-Scanner, Trivy, pip-audit, `npm audit`…) and collapses them into one triaged, de-duplicated finding list with fixes.
- **Harden a box** — a read-only, severity-scored posture audit (firewall, SSH, listeners, world-writable files, updates).
- **Drive your desktop & shell** — launches apps, types, clicks, reads the screen with OCR, and runs your shell behind the safety floor.
- **Bend to your workflow** — writes and sandbox-tests its own Python tools, connects external tool servers over MCP, remembers across sessions, and talks and listens for hands-free work.

*Full tool reference: [`BASILISK_MANUAL.md`](BASILISK_MANUAL.md).*

<br>

---

## Benchmark

Anyone can claim their agent hacks. Basilisk puts a **reproducible number** on it — one you can regenerate yourself in about ten minutes with the commands below — instead of a demo reel and a vibe. Two benchmarks, hardest first.

### The hard one: Juice Shop challenge scoreboard — 51 / 113 solved (45%), fully autonomous

*Full challenge set, `NODE_ENV=unsafe`, fully autonomous & black-box, 2026-07-06. Measured on the autonomous solving engine that ships in v5.2.0 (unchanged since v5.1.2 — every release since only added the injection firewall, the security hardening in this release, and memory fixes; none of it touches how challenges are solved, which is done black-box through the exploit builders + `run`, not through any web reader).*

OWASP Juice Shop ships 100+ individual hacking challenges rated 1–6 stars, and
the app itself tracks which ones you've solved — it only marks a challenge solved
when the exploit **genuinely works**. That makes this the real, hard, comparable
benchmark the security community uses: unlike a vuln-class checklist, it can't be
passed by recall, and it's graded by difficulty. Human CTF players and other
tools report their numbers against the same scoreboard.

Left to run **fully autonomously** — pointed at the target and turned loose, with
no per-command approval and no human clicking — Basilisk solved **51 of the 113
available challenges (45%)**:

| Difficulty | Solved | Rate |
|---|---|---|
| ★ | 9 / 13 | 69% |
| ★★ | 10 / 18 | 56% |
| ★★★ | 13 / 26 | 50% |
| ★★★★ | 8 / 25 | 32% |
| ★★★★★ | **10 / 19** | **53%** |
| ★★★★★★ | 1 / 12 | 8% |

Hardest cracked: **Login Support Team** (6★).

**What this number means, and why the shape matters.** This was a **pure
black-box run** — Basilisk had no access to Juice Shop's source (the source files
aren't even on the machine); it exploited everything from the outside, the same
way other tools and human CTF players are scored. **45% fully autonomous and
black-box on the *full* board is a strong result** — published research puts
fully-autonomous LLM pentest agents in roughly the 20–30% range on comparable
tasks, so this is meaningfully above that, unattended, with a receipt for every
move. And the shape is the interesting part: the **5★ tier lands at 10 of 19
(53%)** — a *higher* solve rate than the 4★ tier (32%) below it, and level with
3★ (50%). A hard tier being the strong point, not the weak one, is the payoff of
the exploit builders mapping directly onto specific challenges — JWT forgery
(*Unsigned JWT*), the security-question password resets (*Reset Bjoern's /
Morty's Password*, *Change Bender's Password*), leaked-secret recon (*Leaked API
Key*, *Leaked Access Logs*, *Email Leak*), and supply-chain / typosquatting
analysis (*Frontend Typosquatting*, *Blockchain Hype*). So Basilisk isn't just
clearing easy wins and stalling: it holds ~50% straight through the middle and
into the hard-exploit tier, and even takes a 6★.

**Where it stops, honestly.** The top of the board is the ceiling — 6★ (8%) and
the harder half of 4★. Challenges needing full RCE/SSTi/SSRF chains, DoS
conditions, or multi-step business-logic abuse (*SSRF*, *SSTi*, *Successful RCE
DoS*, *Wallet Depletion*, *Arbitrary File Write*) are still red — as you'd
expect; those are brutal, and a human expert doesn't clear the whole board
either. This is **not** a claim to beat any specific tool — nobody's published a
like-for-like scoreboard number on the same version. It's an honest, reproducible
measure of where Basilisk actually stands: strong and autonomous from the easy
tiers all the way into the hard-exploit tier, with the full-chain RCE class at
the very top as the clear place left to grow.

Score it yourself:

```bash
docker run -d -p 3000:3000 -e NODE_ENV=unsafe --name juiceshop bkimminich/juice-shop
```

Then turn Basilisk loose on the board and call `juiceshop_report`, which reads the
live scoreboard (`/api/Challenges`) and reports solved/available by difficulty.
Full scorecard: [`benchmarks/juice-shop-scoreboard-2026-07-06.txt`](benchmarks/juice-shop-scoreboard-2026-07-06.txt).

#### How the autonomous run works — the 5.x arsenal (black-box)

No source access, no cheating — Basilisk worked the board from the outside. 5.x
runs a feedback loop plus per-class exploit builders, so the agent can tell
whether an attempt landed, retry intelligently, and keep going on its own:

- **Closed-loop harness** — `juiceshop_score` reads the live board, `juiceshop_next`
  returns what's still unsolved (easiest-first, each mapped to the tool that
  solves it, carrying its live objective + hint from the public scoreboard;
  `per_tier` gives a focused ~30-challenge board), and `juiceshop_diff` confirms a
  hit by diffing the board. The agent works the board → tries a target → confirms
  → moves on.
- **Class exploit builders** — `jwt_forge` (alg:none + RS256→HS256 confusion),
  `nosql_injection`, `xxe_payload`, `coupon_forge` (z85), `captcha_solve`
  (auto-reads the arithmetic CAPTCHA), `reset_password` (security-question flow,
  demo accounts only) — the same model as `sqlmap_plan`.
- **Recon sweep** — `webapp_recon` enumerates the high-signal leak surface
  (`/ftp`, `/encryptionkeys/jwt.pub`, exposed config/logs/backups, the SPA bundle)
  so the leaked-key / backup challenges stop failing on missed recon.

The distribution shows it working: on an earlier one-shot run (before the loop),
the 5★ tier was 1/19. With the closed loop and the builders, it's **10/19** — that
jump is the feedback loop and the exploit builders doing their job, entirely
black-box.

### The methodology check: OWASP vuln-class coverage — 14 / 14 (F1 0.95)

A separate, easier run confirms the workflow end to end: Basilisk found and
confirmed all 14 OWASP vuln *classes* on Juice Shop (SQLi, DOM/stored/reflected
XSS, broken access control, sensitive data exposure, misconfig, directory
listing, mass assignment, vulnerable components, input validation, SSRF, XXE,
JWT deserialization). This proves the orchestration and scoring are sound — but
Juice Shop is heavily documented, so a high coverage score is partly recall.
That's exactly why the scoreboard number above is the one that counts.

**On comparing to other tools:** run your tool of choice against the same Juice
Shop, score it the same way, and compare — `benchmark_compare` (coverage) and the
scoreboard both give like-for-like numbers. Published figures we didn't measure
aren't in this README; an honest, reproducible number beats a marketing table.


<br>

---

## Security — the surface an attacker can reach, cut to the bone

An agent that reads the outside world *and* runs shell commands is a prompt-injection target. Most tools bolt on a filter and hope it holds. Basilisk takes the doors off the building instead.

- **The injection surface was removed, then gated.** The tools that fetched *attacker-chosen* URLs are gone. What's left, `web_read`, reads only from a fixed allow-list, split into two tiers **in code**: **trusted** sources an attacker can't plant content in (NVD, MITRE, CISA, vendor advisories, reputable news) fetch automatically; **community** sources that are user-authored (GitHub, GitLab, Stack Overflow, Wikipedia, PyPI, npm, exploit-db) are held **outside the autonomous loop** — Basilisk can't read one on its own. It raises a **one-tap approval request** in the notification bell; you Allow it (unlocking that source for the session) or ignore it, and either way the run keeps going. This is enforced in the dispatch path, not asked of the model — a compromised model still can't reach a user-authored source without your click. Everything fetched is shielded, arbitrary URLs and off-list redirects are refused, and link-local / cloud-metadata addresses are blocked.
- **The irreversible class can never run.** A structural detector hard-blocks disk/filesystem wipes, recursive root/`$HOME` deletes, fork bombs and raw block-device writes — *before* the shell, in every mode including autonomous, seeing through quoting, `$IFS` and `bash -c` tricks a regex misses. There is no "Run anyway" and no setting that disables it.
- **Untrusted input is quarantined.** Anything from outside — a target's response, an MCP result, an analyzed image — is run through a deterministic content firewall and wrapped as *data, never instructions.*
- **Your sudo password never touches the model**, self-written code runs only in a **bubblewrap jail** after passing its own test, and Basilisk's own safety code can't be overwritten by a shell command.

All of it is pinned in the test suite. It writes and runs real exploits against authorized targets — that's the job — but it will not churn out standalone weaponized malware (reverse shells, implants, ransomware, backdoors), and the destructive class can never run through it at all.

<br>

---

## Get an API key

Basilisk is multi-provider — you only need a key for the one you want. Set it in **Settings → Backends**.

| Provider | Get a key | Notes |
| --- | --- | --- |
| **SiliconFlow** | <https://cloud.siliconflow.com/account/ak> | **Default.** Big open models (DeepSeek, Qwen, Kimi) + SenseVoice STT |
| **Groq** | <https://console.groq.com/keys> | Blistering speed, generous free tier, Whisper STT. Keys look like `gsk_...` |

Keys live only in `~/.config/kali/settings.json`, locked to your user — they never go anywhere but the provider's own API.

<br>

---

<div align="center">

## License

**MIT.** Take it, fork it, ship it.

## Credits

Forged by **The Priest** ⟁

*A dragon that lives on your machine, answers only to you, and never forgets where the bodies are buried.*

</div>
