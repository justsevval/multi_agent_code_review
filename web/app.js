const elCode = document.getElementById("code");
const elResults = document.getElementById("results");
const elStatus = document.getElementById("status");
const elSummary = document.getElementById("summary");
const elMeta = document.getElementById("meta");
const elPretty = document.getElementById("pretty");

const btnAnalyze = document.getElementById("btnAnalyze");
const btnClear = document.getElementById("btnClear");
const btnExample = document.getElementById("btnExample");
const btnCopy = document.getElementById("btnCopy");

let lastJson = null;

function setStatus(text, busy = false) {
  elStatus.textContent = text;
  btnAnalyze.disabled = busy;
  btnClear.disabled = busy;
  btnExample.disabled = busy;
}

function sevClass(sev) {
  const s = (sev || "").toLowerCase();
  if (s === "high") return "high";
  if (s === "medium") return "medium";
  return "low";
}

function renderEmpty() {
  elResults.classList.add("empty");
  elResults.innerHTML = `
    <div class="emptyState">
      <div class="emptyTitle">Analiz çıktısı burada görünecek</div>
      <div class="emptyText">Bir kod ekleyip <b>Analyze</b>’a bas.</div>
    </div>
  `;
  elSummary.textContent = "Henüz analiz yapılmadı.";
  elMeta.textContent = "";
  btnCopy.disabled = true;
}

function renderIssues(json) {
  const issues = json?.issues || [];
  elResults.classList.remove("empty");

  if (!issues.length) {
    elResults.innerHTML = `
      <div class="emptyState">
        <div class="emptyTitle">Sorun bulunamadı ✅</div>
        <div class="emptyText">Kurallarımıza göre belirgin bir problem tespit edilmedi.</div>
      </div>
    `;
    elSummary.textContent = "0 issue bulundu.";
  } else {
    const counts = { high: 0, medium: 0, low: 0 };
    issues.forEach((i) => counts[sevClass(i.severity)]++);

    elSummary.textContent = `${issues.length} issue bulundu — High: ${counts.high}, Medium: ${counts.medium}, Low: ${counts.low}`;

    elResults.innerHTML = issues
      .map(
        (i) => `
      <div class="card">
        <div class="row">
          <div class="badges">
            <span class="badge">${i.agent || "Agent"}</span>
            <span class="badge ${sevClass(i.severity)}">${(
          i.severity || "low"
        ).toUpperCase()}</span>
          </div>
        </div>
        <div class="msg">${escapeHtml(i.message || "")}</div>
        <div class="small">Tip: Bu bulguyu düzeltmek için kodu daha küçük parçalara ayırmayı ve güvenli fonksiyonlar kullanmayı düşün.</div>
      </div>
    `
      )
      .join("");
  }

  btnCopy.disabled = false;
  elMeta.textContent = `Son analiz: ${new Date().toLocaleTimeString()}`;
}

function escapeHtml(str) {
  return str
    .replaceAll("&", "&amp;")
    .replaceAll("<", "&lt;")
    .replaceAll(">", "&gt;");
}

async function analyze() {
  const code = elCode.value || "";
  if (!code.trim()) {
    setStatus("Kod boş. Lütfen kod yapıştır.", false);
    return;
  }

  setStatus("Analiz ediliyor…", true);

  try {
    const res = await fetch("/review", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ code }),
    });

    const json = await res.json();
    lastJson = json;

    if (!res.ok) {
      renderIssues({
        issues: [
          {
            agent: "API",
            severity: "high",
            message: json?.detail || "Request failed",
          },
        ],
      });
      setStatus("Hata oluştu.", false);
      return;
    }

    renderIssues(json);
    setStatus("Bitti ✅", false);
  } catch (err) {
    renderIssues({
      issues: [{ agent: "Client", severity: "high", message: String(err) }],
    });
    setStatus("Bağlantı hatası.", false);
  }
}

function loadExample() {
  const examples = [
    `# Example 1: Nested loops + eval
def calc(items):
    total = 0
    for i in range(len(items)):
        for j in range(len(items)):
            total += items[i] * items[j]
    return total

eval("print('hi')")
`,
    `# Example 2: Long line (PEP8) + exec
def very_long_line():
    print("This is a very very very very very very very very very very very very very very long line that breaks 79 chars")

exec("print('running')")
`,
    `# Example 3: subprocess shell=True risk
import subprocess

def run_cmd(user_input):
    subprocess.Popen("echo " + user_input, shell=True)
`,
    `# Example 4: Simple clean code (should find few issues)
def add(a, b):
    \"\"\"Return sum of two numbers.\"\"\"
    return a + b
`,
    `# Example 5: Deep nesting
def check(x):
    if x > 0:
        if x % 2 == 0:
            if x > 10:
                return "big even"
    return "other"
`,
    `# Example 6: Syntax error example
def broken(
    print("oops")
`,
    `# Example 7: Many prints (style / maintainability idea)
def debug():
    for i in range(3):
        print("debug", i)
    print("done")
`,
  ];

  const choice = examples[Math.floor(Math.random() * examples.length)];
  elCode.value = choice;
}

function clearAll() {
  elCode.value = "";
  lastJson = null;
  renderEmpty();
  setStatus("Hazır", false);
}

async function copyJson() {
  if (!lastJson) return;
  const pretty = elPretty.checked;
  const txt = pretty
    ? JSON.stringify(lastJson, null, 2)
    : JSON.stringify(lastJson);
  await navigator.clipboard.writeText(txt);
  setStatus("JSON kopyalandı ✅", false);
  setTimeout(() => setStatus("Hazır", false), 900);
}

btnAnalyze.addEventListener("click", analyze);
btnExample.addEventListener("click", () => {
  loadExample();
  setStatus("Örnek yüklendi.", false);
});
btnClear.addEventListener("click", clearAll);
btnCopy.addEventListener("click", copyJson);

renderEmpty();
