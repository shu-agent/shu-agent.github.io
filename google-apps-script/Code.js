// Google Apps Script - 手紙をSpreadsheetに読み書き
// アクセス許可: 全員

const SPREADSHEET_ID = 'YOUR_SPREADSHEET_ID';

// 手紙受信用（POST）
function doPost(e) {
  try {
    let data = JSON.parse(e.postData.contents);

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

// 手紙一覧取得用（GET）
function doGet(e) {
  try {
    const sheet = SpreadsheetApp.openById(SPREADSHEET_ID).getSheetByName('letters');
    const data = sheet.getDataRange().getValues();

    const letters = data.slice(1).map(row => ({
      timestamp: row[0],
      recipient: row[1],
      sender: row[2],
      message: row[3],
      status: row[4]
    }));

    return ContentService
      .createTextOutput(JSON.stringify({ letters }))
      .setMimeType(ContentService.MimeType.JSON);

  } catch (err) {
    return ContentService
      .createTextOutput(JSON.stringify({ status: 'error', message: err.message }))
      .setMimeType(ContentService.MimeType.JSON);
  }
}