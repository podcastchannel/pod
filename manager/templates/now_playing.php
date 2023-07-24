<?php

//max recent tracks to keep in the recently played tracks history
$max_recent = 5;

echo('omar');

//secret key to access the script
$key = 'TB21Dr3km';

//check access
if ($_REQUEST['key'] !== $key) {
    ReturnError(400, 'Invalid key');
}

//retrieve title info
$title = htmlspecialchars($_REQUEST['casttitle']);

//save current track title and update history
$file = 'now_playing.txt';
$recent = file($file, FILE_IGNORE_NEW_LINES | FILE_SKIP_EMPTY_LINES);
$recent = array_slice($recent, 0, $max_recent);

$r = fopen($file, 'wb');
if ($r !== false) {
    //current track
    fwrite($r, $title . "\n");
    //recent tracks
    foreach ($recent as $s) {
        fwrite($r, $s . "\n");
    }
    fclose($r);
} else {
    ReturnError(500, 'Failed to save track title');
}

//album cover
$artwork = isset($_REQUEST['artwork']) && ($_REQUEST['artwork'] !== '') ? $_REQUEST['artwork'] : false;
if ($artwork !== false) {
    $artwork = base64_decode($artwork);
    $r = fopen('https://res.cloudinary.com/dvnemzw0z/image/upload/v1690211697/nowplaying_artwork_fasavn.png', 'wb');
    if ($r !== false) {
        fwrite($r, $artwork);
        fclose($r);
    } else {
        ReturnError(500, 'Failed to save track artwork');
    }
}

function ReturnError($code, $text) {
    $protocol = isset($_SERVER['SERVER_PROTOCOL']) ? $_SERVER['SERVER_PROTOCOL'] : 'HTTP/1.0';
    header($protocol . ' ' . $code . ' ' . $text);
    exit();
}