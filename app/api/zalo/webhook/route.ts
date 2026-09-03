import { NextRequest, NextResponse } from 'next/server';

const gasWebhookUrl = process.env.GAS_WEB_APP_URL;

export async function POST(request: NextRequest) {
  if (!gasWebhookUrl) {
    return NextResponse.json(
      { error: 'Missing GAS_WEB_APP_URL environment variable' },
      { status: 500 }
    );
  }

  const body = await request.text();

  try {
    const response = await fetch(gasWebhookUrl, {
      method: 'POST',
      headers: {
        'Content-Type': request.headers.get('content-type') ?? 'application/json',
      },
      body,
      redirect: 'follow',
    });

    return NextResponse.json(
      { message: 'Webhook forwarded to Apps Script' },
      { status: response.ok ? 200 : 502 }
    );
  } catch (error) {
    console.error('Cannot forward webhook to Apps Script:', error);

    return NextResponse.json(
      { error: 'Cannot forward webhook to Apps Script' },
      { status: 502 }
    );
  }
}

export async function GET() {
  return NextResponse.json({
    status: 'Zalo webhook proxy is running',
  });
}
