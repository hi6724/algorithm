const TIER = ['bronze', 'silver', 'gold', 'platinum', 'diamond'];

function downloadJson(data) {
  const jsonString = JSON.stringify(data, null, 2);
  const blob = new Blob([jsonString], { type: 'application/json' });
  const url = URL.createObjectURL(blob);
  const a = document.createElement('a');
  a.href = url;
  a.download = 'data.json';
  document.body.appendChild(a);
  a.click();
  document.body.removeChild(a);
  URL.revokeObjectURL(url);
  data.forEach((el) => {
    window.open(`https://www.acmicpc.net/source/download/${el.id}`);
  });
}

function printTbodyChildren(tbody) {
  let rows = tbody.querySelectorAll('tr');
  let results = [];

  rows.forEach((row) => {
    let id = row.id.split('-')[1];
    let problemId = row.querySelector('td:nth-child(3) > a').textContent.trim();
    let problemTitle = row.querySelector('td:nth-child(3) > a').dataset.originalTitle;
    let language = row.querySelector('td:nth-child(7) > a').textContent.trim();
    let submissionDate = row.querySelector('td:nth-child(9) > a').dataset.originalTitle;
    let tier = row.querySelector('.solvedac-tier').src.split('tier/')[1].split('.svg')[0];
    const tierName = TIER[Math.floor((+tier - 1) / 5)];
    const tierCnt = 5 - ((+tier - 1) % 5);

    let file_name = 'py3';
    if (language.toLowerCase().includes('java')) {
      file_name = 'java';
    } else if (language.toLowerCase().includes('node')) {
      file_name = 'js';
    } else if (language.toLowerCase().includes('c++')) {
      file_name = 'cc';
    }

    let result = {
      id: id,
      problemId: problemId,
      problemTitle: problemTitle,
      language: language,
      submissionDate: submissionDate,
      file_name: `${id}.${file_name}`,
      tier: `${tierName}_${tierCnt}`,
    };

    results.push(result);
  });
  return results;
}

function openNextPage(href) {
  var newWindow = window.open(href, '_blank');

  newWindow.onload = function () {
    var tbody = newWindow.document.querySelector('tbody');
    var nextPageLink = newWindow.document.getElementById('next_page');
    var nextHref = null;
    var tbodyContent = null;
    if (nextPageLink) nextHref = nextPageLink.getAttribute('href');
    if (tbody) tbodyContent = printTbodyChildren(tbody);

    newWindow.opener.postMessage({ type: 'BOJ_SCRIPT', tbody: tbodyContent, href: nextHref }, '*');

    newWindow.close();
  };
}

window.addEventListener('message', function ({ data }) {
  if (data?.type !== 'BOJ_SCRIPT') return;
  const { href, tbody } = data;
  rootData.push(...tbody);
  if (href) openNextPage(href);
  if (!href) downloadJson(rootData);
});

function initPage(id) {
  const url = `https://www.acmicpc.net/status?user_id=${id}&result_id=4`;
  if (location.href !== url) {
    location.href = url;
    return;
  }

  const nextLink = window.document.getElementById('next_page');
  const tbody = window.document.querySelector('tbody');
  if (tbody) rootData.push(...printTbodyChildren(tbody));

  if (nextLink) {
    const nextHref = nextLink.getAttribute('href');
    openNextPage(nextHref);
  } else {
    downLoadJson(rootData);
  }
}

const rootData = [];
// 자신의 ID 넣어서 실행
initPage('hi6724');
