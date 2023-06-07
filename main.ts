radio.onReceivedString(function (receivedString) {
    if (receivedString == "C") {
        모션()
        radio.sendString("D")
    }
})
function 모션 () {
	
}
