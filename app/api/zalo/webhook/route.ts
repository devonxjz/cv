import { NextRequest, NextResponse } from 'next/server';

export async function POST(request: NextRequest) {
  try {
    const payload = await request.json();
    console.log('Zalo webhook payload:', JSON.stringify(payload));
  } catch {
    console.log('Zalo webhook: received non-JSON or empty POST request');
  }

  return NextResponse.json({ message: 'OK' }, { status: 200 });
}

export async function GET() {
  return NextResponse.json({ status: 'Zalo webhook is running' });
}
