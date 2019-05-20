var AudioContextFunc = window.AudioContext || window.webkitAudioContext;
var audioContext = new AudioContextFunc();
var player=new WebAudioFontPlayer();
console.log("player", player);
player.loader.decodeAfterLoading(audioContext, 'castle.midi');

function play() {
  player.queueWaveTable(audioContext, audioContext.destination
    , _tone_0250_SoundBlasterOld_sf2, 0, 12*4+7, 2);
  return false;
}
