// Google Apps Script - 手紙をSpreadsheetに書き込む
// 部署: Web Appとして公開（アクセス許可: 全員）

const SPREADSHEET_ID = 'YOUR_SPREADSHEET_ID';

// CORS対応のためdoPostとdoGet両対応
function doPost(e) {
  return handleRequest(e);
}

function doGet(e) {
  return handleRequest(e);
}

function handleRequest(e) {
  try {
    let data;
    if (e.method === 'POST' || e.postData) {
      data = JSON.parse(e.postData.contents);
    } else {
      data = e.parameter;
    }

    const sheet = SpreadsheetApp.openById(SPREADSHEET_ID).getSheetByName('letters');

    sheet.appendRow([
      new Date(),
      data.recipient || '',
      data.sender || '名無しの住人',
      data.message || '',
      'unread'
    ]);

    return ContentService
      .createTextOutput(JSON.stringify({ status: 'success' }))
      .setMimeType(ContentService.MimeType.JSON);

  } catch (err) {
    return ContentService
      .createTextOutput(JSON.stringify({ status: 'error', message: err.message }))
      .setMimeType(ContentService.MimeType.JSON);
  }
}

// 住人が手紙を確認したらステータスを更新
function markAsRead(row) {
  const sheet = SpreadsheetApp.openById(SPREADSHEET_ID).getSheetByName('letters');
  sheet.getRange(row, 5).setValue('read');
}

// 住人が返信を書き込み
function appendReply(recipient, replyMessage) {
  const sheet = SpreadsheetApp.openById(SPREADSHEET_ID).getSheetByName('replies');
  sheet.appendRow([
    new Date(),
    recipient,
    replyMessage
  ]);
}