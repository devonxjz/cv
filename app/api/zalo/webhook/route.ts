import { NextRequest, NextResponse, after } from 'next/server';

export async function POST(request: NextRequest) {
  const gasWebhookUrl = process.env.GAS_WEB_APP_URL;
  const contentType = request.headers.get('content-type') ?? 'application/json';

  let body = '';
  try {
    body = await request.text();
    console.log('Zalo webhook received payload:', body || '(empty body)');
  } catch (err) {
    console.error('Error reading webhook body:', err);
  }

  // Forward asynchronously to Google Apps Script in the background
  // to ensure Zalo gets an immediate 200 OK and avoids 408 Timeout.
  if (gasWebhookUrl) {
    after(async () => {
      try {
        console.log('Forwarding to Google Apps Script...');
        const response = await fetch(gasWebhookUrl, {
          method: 'POST',
          headers: {
            'Content-Type': contentType,
          },
          body,
          redirect: 'follow',
        });
        console.log('GAS responded with status:', response.status);
      } catch (forwardError) {
        console.error('Cannot forward webhook to Apps Script:', forwardError);
      }
    });
  } else {
    console.warn('GAS_WEB_APP_URL environment variable is not defined.');
  }

  return NextResponse.json(
    { message: 'OK', forwarded: Boolean(gasWebhookUrl) },
    { status: 200 }
  );
}

export async function GET() {
  return NextResponse.json({
    status: 'Zalo webhook proxy is running',
  });
}
