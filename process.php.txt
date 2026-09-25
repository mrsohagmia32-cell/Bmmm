<?php
header('Content-Type: application/json');

// আপনার গোপনীয় এপিআই কি এবং প্যানেল ইউআরএল (এখানে সুরক্ষিত থাকবে)
define('API_KEY', '00872f5f0b0c75305cc49069d7691006');
define('API_URL', 'https://likefollowerbuy.com/api/v2');

$action = $_POST['action'] ?? '';

function callSMM($postData) {
    $postData['key'] = API_KEY;
    $ch = curl_init();
    curl_setopt($ch, CURLOPT_URL, API_URL);
    curl_setopt($ch, CURLOPT_RETURNTRANSFER, 1);
    curl_setopt($ch, CURLOPT_POST, 1);
    curl_setopt($ch, CURLOPT_POSTFIELDS, http_build_query($postData));
    curl_setopt($ch, CURLOPT_SSL_VERIFYPEER, 0);
    curl_setopt($ch, CURLOPT_SSL_VERIFYHOST, 0);
    $output = curl_exec($ch);
    curl_close($ch);
    return json_decode($output, true);
}

if ($action === 'balance') {
    $res = callSMM(['action' => 'balance']);
    echo json_encode($res);
} 
elseif ($action === 'services') {
    $res = callSMM(['action' => 'services']);
    echo json_encode($res);
} 
elseif ($action === 'add') {
    $service = $_POST['service'] ?? '';
    $link = $_POST['link'] ?? '';
    $quantity = $_POST['quantity'] ?? '';

    if (empty($service) || empty($link) || empty($quantity)) {
        echo json_encode(['error' => 'সব ফিল্ড পূরণ করুন']);
        exit;
    }

    $res = callSMM([
        'action' => 'add',
        'service' => $service,
        'link' => $link,
        'quantity' => $quantity
    ]);
    echo json_encode($res);
} else {
    echo json_encode(['error' => 'Invalid action']);
}
?>
