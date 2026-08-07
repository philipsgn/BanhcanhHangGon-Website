const NTFY_TIMEOUT_MS = 10000;

function formatPrice(value) {
  return `${value.toLocaleString('vi-VN')} VNĐ`;
}

function buildNtfyBody(order) {
  const isDelivery = order.order_type === 'delivery';

  const itemLines =
    Array.isArray(order.items) && order.items.length > 0
      ? order.items.map(item => `• ${item.name} × ${item.quantity}`).join('\n')
      : '(không có thông tin món)';

  const lines = [
    'ĐƠN ĐẶT MỚI',
    '',
    `Khách: ${order.customer_name ?? '—'}`,
    `Điện thoại: ${order.phone ?? '—'}`,
    `Nhận: ${isDelivery ? 'Giao hàng' : 'Đến lấy tại quán'}`,
  ];

  if (isDelivery && order.address) {
    lines.push(`Địa chỉ: ${order.address}`);
  }

  lines.push(
    '',
    'Món:',
    itemLines,
    '',
    `Tổng: ${formatPrice(order.total_amount ?? 0)}`
  );

  return lines.join('\n');
}


export async function sendNtfyNotification(order) {

  console.log("NTFY VERSION TEST 20260807");

  const topic = process.env.NTFY_TOPIC?.trim();

  if (!topic) {
    return {
      success:false,
      error:'NTFY_TOPIC missing'
    };
  }

  const baseUrl =
    process.env.NTFY_BASE_URL?.trim() ??
    'https://ntfy.sh';

  const url = `${baseUrl}/${topic}`;


  const controller = new AbortController();

  const timeoutId = setTimeout(
    () => controller.abort(),
    NTFY_TIMEOUT_MS
  );


  try {

    const response = await fetch(url,{
      method:'POST',

      headers:{
        'Content-Type':'text/plain; charset=utf-8',
        'Title':'🍜 Đơn hàng mới',
        'Priority':'urgent',
        'Tags':'shopping_cart,restaurant',
        'User-Agent':'BanhCanhHangGon-Website/1.0'
      },

      body:buildNtfyBody(order),

      signal:controller.signal
    });


    clearTimeout(timeoutId);


    if(!response.ok){

      const detail =
        await response.text().catch(()=>'');

      return {
        success:false,
        error:`ntfy ${response.status}: ${detail}`
      };
    }


    return {
      success:true
    };


  } catch(err){

    clearTimeout(timeoutId);

    console.error(
      "NTFY FAILED:",
      err
    );


    return {
      success:false,
      error:`ntfy network error: ${
        err?.name
      }: ${
        err?.message
      }`
    };
  }
}