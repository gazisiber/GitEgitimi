---
marp: true
theme: default
class: invert
paginate: true
style: |
  /* Genel Arka Plan ve Metin Rengi (Nord - Polar Night & Snow Storm) */
  :root {
    --color-background: #2E3440;
    --color-foreground: #D8DEE9;
  }
  section {
    background-color: var(--color-background);
    color: var(--color-foreground);
  }
  
  /* Başlık Renkleri (Nord - Frost) */
  h1 { color: #88C0D0; }
  h2, h3 { color: #81A1C1; }

  /* Kod Blokları (Nord) */
  pre {
    background-color: #3B4252 !important;
    border: 2px solid #4C566A;
    border-radius: 8px;
    box-shadow: 0 4px 10px rgba(0,0,0,0.4);
  }
  
  /* Metin içi (inline) kodlar */
  code {
    background-color: #434C5E;
    color: #EBCB8B; /* Nord Sarısı - Ayrıştırmak için */
    padding: 3px 6px;
    border-radius: 4px;
    border: 1px solid #4C566A;
  }
  
  /* pre içindeki code etiketinin sıfırlanması */
  pre > code {
    border: none;
    padding: 0;
    background-color: transparent;
    color: #D8DEE9;
  }

  .center-images {
    display: flex;
    justify-content: center;
    align-items: center;
    height: 100%;
    gap: 20px;
  }

  /* Kapak Sayfası Özel Sınıfları */
  .cover-date { position: absolute; bottom: 100px; left: 60px; font-size: 22px; color: #81A1C1; }
  .cover-footer-left { position: absolute; bottom: 50px; left: 60px; font-size: 20px; color: #E5E9F0; opacity: 0.8; }
  .cover-footer-right { position: absolute; bottom: 50px; right: 60px; font-size: 20px; color: #E5E9F0; opacity: 0.8; text-align: right; }
---

# Git Versiyon Kontrol Sistemi

</div>

<div class="cover-image-area">

<img src="https://git-scm.com/images/logos/downloads/Git-Icon-1788C.png" alt="Git Logo" width="100px"/>

</div>

</div>  

<div class="cover-date">9 Mart 2026</div>
<div class="cover-footer-left">Aliberk Sandıkçı</div>
<div class="cover-footer-right">Gazi Siber - Eğitim ve ARGE Birimi</div>

---

# Eğitime Hazırlık

- Git Eklentisi olan Kod Editörü / IDE
  - VS Code
  - Zed
- Bilgisayarı olmayanlar için: Termux

---

# Eğitime Hazırlık
- Git Kurulumu
  - Linux: `sudo apt install git` (kendi paket yöneticinizi kullanınız)
  - Mac: `brew install git`
  - Windows: `winget install Git.Git`
- GitHub Aracı Kurulumu
  - Linux: `sudo apt install gh` (kendi paket yöneticinizi kullanınız)
  - Mac: `brew install gh`
  - Windows: `winget install GitHub.cli`
- Doğrulama
  - `git --version`
  - `gh --version`

---

# Git Eğitimi - _Meta_

<div class="center-images">
  <img src="eg_arge.jpg" width="400">
  <img src="image.png" width="400">
</div>

---

# Git Nedir ve Neden Kullanılır?

Git **dağıtık** bir **Versiyon Kontrol Sistemi**dir (VCS) Bireysel projelerin veya ekiplerin geliştirme sürecini daha organize hâle getirir.

Başta Linux'un geliştirilme süreci için Linus Torvalds tarafından yazılmıştır.

---

![image2.png](image2.png)

---

# 2. Git "Hub" nedir?
GitHub git repolarının (depo/proje) depolandığı uzak sunuculardan yalnızca biri
- GitHub
- GitLab
- Codeberg
- cgit

---

![image4.png](image4.png)

---

<div class="center-images">
  <img src="image5.png" width="800">
</div>

---

# 3. Neler neler var?

```bash
git <komut> [<argümanlar>]
```

```bash
git clone https://github.com/gazisiber/GitEgitimi
```

`clone` `init` `remote`
`add` `rm` `commit`
`push` `pull` `fetch`
`diff` `status` `log`
`stash` `branch` `merge` `checkout`

---

# Kaynaklar

```bash
git --help
man git
tldr git
```

- [Explain Shell](https://explainshell.com/)
- [Resmi Git Dokümanı](https://git-scm.com/docs/user-manual.html)
- [Etkileşimli Git Çalışma Mantığı](https://learngitbranching.js.org/)


---

# Son Hazırlıklar

- GitHub hesabı açalım
- Git bilgilerimizi yerelde girelim

```bash
git config --global user.name "Ad Soyad"
```

```bash
git config --global user.email "mail@domain.tld"
```

---

# Örnek


---

![image3](image3.png)

---

# Etkileşimli Devam edelim :)
