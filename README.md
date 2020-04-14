# threefive

## Full disclosure statement: I Gonzo'ed the pip builds 2.0.63 and 2.0.65, please update to 2.0.69. 
## I apologize for my mistakes.

## SCTE35 Decoder
*  Parse SCTE 35 messages from Mpeg Transport Streams and Binary files. 
*  Parse SCTE 35 messages encoded in Base64, Binary, or Hex. 

### Fast Start Directions.
*  ['Up and Running in Less Than Seven Seconds'](https://github.com/futzu/SCTE35-threefive/blob/master/FastStart.md) 


### 2019 Specification 
[SCTE35 2019 specification](https://scte-cms-resource-storage.s3.amazonaws.com/ANSI_SCTE-35-2019a-1582645390859.pdf)
###  Splice Commands 
- [x] Splice Null  
- [x] Splice Schedule  (lightly tested)
- [x] Splice Insert 
- [x] Time Signal 
- [x] Bandwidth Reservation  (lightly tested)
###  Splice Descriptors 
- [x]  DTMF Descriptor 
- [x]  Segmentation Descriptor
- [x]  Segmentation UPID  (partially implemented)
- [x]  Segmentation Types and Messages 
- [x]  Time Descriptor 
- [x]  Audio Descriptor (lightly tested)

###  Dependencies 
- [x] Python 3
- [x] bitn

##  Install 
```
pip install threefive
Collecting threefive
  Downloading threefive-2.0.69-py3-none-any.whl (12 kB)
Collecting bitn>=0.0.21
  Downloading bitn-0.0.21-py3-none-any.whl (3.0 kB)
Installing collected packages: bitn, threefive
Successfully installed bitn-0.0.21 threefive-2.0.69

```

##  Using threefive  
#### Call threefive.decode.

- [x]  mpegts files
- [x]  binary files
- [x]  base64 encoded strings
- [x]  hex encoded strings
- [x]  binary byte strings
 

 ####  Parse Mpegts Files 
```python
>>> import threefive
>>> threefive.decode('/path/to/mpegwithscte35.ts') 
```

####  Parse Binary Encoded Messages From a File
```python
>>> import threefive
>>> stuff=threefive.decode('/mnt/build/file.bin')
```

####  Parse Base64 Encoded Messages 
```python
>>> import threefive
>>> mesg='/DBhAAAAAAAA///wBQb+qM1E7QBLAhdDVUVJSAAArX+fCAgAAAAALLLXnTUCAAIXQ1VFSUg/nwgIAAAAACyy150RAAACF0NVRUlIAAAnf58ICAAAAAAsstezEAAAihiGnw=='
>>> t=threefive.decode(mesg)
```

####  Parse Hex Encoded Messages 

```python
>>> import threefive
>>> u=threefive.decode('0xFC302F000000000000FFFFF014054800008F7FEFFE7369C02EFE0052CCF500000000000A0008435545490000013562DBA30A')
```

#### Parse Binary Byte String Messages
```python
>>> import threefive
>>> f=open('/mnt/build/file.bin','rb').read()
>>> scte35=threefive.decode(f)
```

### Output for Base64 and Hex Strings
- [x] SCTE 35 Info Section
- [x] SCTE 35 Command
- [x] SCTE 35 Descriptors

```js
{   'SCTE35': {   'Info_Section': {   'crc': '0x62dba30a',
                                      'cw_index': '0xff',
                                      'descriptor_loop_length': 10,
                                      'encrypted_packet': False,
                                      'encryption_algorithm': 0,
                                      'private': False,
                                      'protocol_version': 0,
                                      'pts_adjustment': '0.000000',
                                      'reserved': 3,
                                      'section_length': 47,
                                      'section_syntax_indicator': False,
                                      'splice_command_length': 20,
                                      'splice_command_type': 5,
                                      'table_id': '0xfc',
                                      'tier': '0xfff'},
                  'Splice_Command': {   'avail_expected': 0,
                                        'avail_num': 0,
                                        'break_auto_return': True,
                                        'break_duration': '60.293567',
                                        'duration_flag': True,
                                        'name': 'Splice '
                                                'Insert',
                                        'out_of_network_indicator': True,
                                        'program_splice_flag': True,
                                        'pts_time': '21514.559089',
                                        'splice_event_cancel_indicator': False,
                                        'splice_event_id': 1207959695,
                                        'splice_immediate_flag': False,
                                        'time_specified_flag': True,
                                        'unique_program_id': 0},
                  'Splice_Descriptors': [   {   'descriptor_length': 8,
                                                'identifier': 'CUEI',
                                                'name': 'Avail '
                                                        'Descriptor',
                                                'provider_avail_id': 309,
                                                'splice_descriptor_tag': 0}]}}

```
### Output for Mpegts streams and Files
- [x] Packet Pid
- [x] Packet PTS
- [x] SCTE 35 Info Section
- [x] SCTE 35 Command
- [x] SCTE 35 Descriptors


```js

{   'Packet': {   'pid': '0x135',
                  'pts': '89977.249522'},
    'SCTE35': {   'Info_Section': {   'crc': '0x6e33321e',
                                      'cw_index': '0x0',
                                      'descriptor_loop_length': 10,
                                      'encrypted_packet': False,
                                      'encryption_algorithm': 0,
                                      'private': False,
                                      'protocol_version': 0,
                                      'pts_adjustment': '0.000000',
                                      'reserved': 3,
                                      'section_length': 42,
                                      'section_syntax_indicator': False,
                                      'splice_command_length': 4095,
                                      'splice_command_type': 5,
                                      'table_id': '0xfc',
                                      'tier': '0xfff'},
                  'Splice_Command': {   'avail_expected': 0,
                                        'avail_num': 0,
                                        'duration_flag': False,
                                        'name': 'Splice '
                                                'Insert',
                                        'out_of_network_indicator': False,
                                        'program_splice_flag': True,
                                        'pts_time': '89984.161689',
                                        'splice_event_cancel_indicator': False,
                                        'splice_event_id': 662,
                                        'splice_immediate_flag': False,
                                        'time_specified_flag': True,
                                        'unique_program_id': 1},
                  'Splice_Descriptors': [   {   'descriptor_length': 8,
                                                'identifier': 'CUEI',
                                                'name': 'Avail '
                                                        'Descriptor',
                                                'provider_avail_id': 0,
                                                'splice_descriptor_tag': 0}]}}

```



###  threefive.Splice.show() 
#### Shows all data
```python
>>> import threefive                
>>> mesg='/DBIAAAAAAAA///wBQb+ky44CwAyAhdDVUVJSAAACn+fCAgAAAAALKCh4xgAAAIX
Q1VFSUgAAAl/nwgIAAAAACygoYoRAAC0IX6w')
>>> fu=threefive.Splice(mesg)
>>> fu.show()
```

###  Read individual values 
```python
>>> import threefive
>>> mesg='/DAvAAAAAAAA///wFAVIAACPf+/+c2nALv4AUsz1AAAAAAAKAAhDVUVJAAABNWLbowo='
>>> scte_data=threefive.Splice(mesg)
>>> scte_data.command.name    
'Splice Insert'
>>> scte_data.command.splice_immediate_flag
False
>>> scte_data.command.pts_time
'21514.559089'
>>> scte_data.command.break_duration
'60.293567'
```
