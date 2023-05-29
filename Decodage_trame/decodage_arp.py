import struct
import datetime
from fonction_decodage import*

def decodage_arp(date2, bench_3, bench_5, framesize, trame, FT):
	(macd1, macd2, macd3, macd4, macd5, macd6,
    macs1, macs2, macs3, macs4, macs5, macs6,
    field_1, field_2, field_3, field_4, field_5, field_6,
    mac_sender1, mac_sender2, mac_sender3, mac_sender4, mac_sender5, mac_sender6,
    sender_ip1, sender_ip2, sender_ip3, sender_ip4,
    mac_target1, mac_target2, mac_target3, mac_target4, mac_target5, mac_target6,
    target_ip1, target_ip2, target_ip3, target_ip4) = struct.unpack_from('>12B3H2BH20B', trame)
 
	macdest = adr_mac(macd1, macd2, macd3, macd4, macd5, macd6)
	macsrc = adr_mac(macs1, macs2, macs3, macs4, macs5, macs6)
	mac_sender = adr_mac(mac_sender1, mac_sender2, mac_sender3, mac_sender4, mac_sender5, mac_sender6)
	sender_ip = adr_ip(sender_ip1, sender_ip2, sender_ip3, sender_ip4)
	mac_target = adr_mac(mac_target1, mac_target2, mac_target3, mac_target4, mac_target5, mac_target6)
	target_ip = adr_ip(target_ip1, target_ip2, target_ip3, target_ip4)

	date_init_framedate = datetime.datetime(1970, 1, 1, 0, 0, 0)
	framedate = date_init_framedate + datetime.timedelta(0, date2)
	framedate = framedate.strftime("%Y-%m-%d %H:%M:%S")
 
	for keys, value in FT['FT_0'].items():
		if bench_5 == keys:
			bench_5 = value

	for keys, value in FT['FT_MAC'].items():
		if macdest == keys:
			macdest = value
   
	for keys, value in FT['FT_MAC'].items():
		if macsrc == keys:
			macsrc = value
	
	for keys, value in FT['FT_MAC'].items():
		if mac_sender == keys:
			mac_sender = value
   
	for keys, value in FT['FT_IP'].items():
		if sender_ip == keys:
			sender_ip = value
	 
	for keys, value in FT['FT_MAC'].items():
		if mac_target == keys:
			mac_target = value
   
	for keys, value in FT['FT_IP'].items():
		if target_ip == keys:
			sender_ip = value

	return (framedate, bench_3, bench_5, framesize, macdest, macsrc, 
         field_1, field_2, field_3, field_4, field_5, field_6, mac_sender, sender_ip, mac_target, target_ip)