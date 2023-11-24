# kill an executing process
$exec_pid = 'killmenow'
exec { 'stop_process':
command => "/usr/bin/pkill -f ${exec_pid}"
}
