"""
encode.py

threefive.encode has helper functions for Cue encoding.

"""


from .commands import SpliceNull, SpliceInsert, TimeSignal
from .cue import Cue


def mk_splice_null():
    """
    mk_splice_null returns a Cue
    with a Splice Null
    """
    cue = Cue()
    sn = SpliceNull()
    cue.command = sn
    cue.encode()
    return cue


def mk_time_signal(pts=None):
    """
     mk_time_signal returns a Cue
     with a Time Signal

     if pts is NOT set:
         time_specified_flag   False

    if pts IS set:
         time_specified_flag   True
         pts_time              pts

    """
    cue = Cue()
    ts = TimeSignal()
    ts.time_specified_flag = False
    if pts:
        pts = float(pts)
        ts.time_specified_flag = True
        ts.pts_time = pts
    cue.command = ts
    cue.encode()
    return cue


def mk_splice_insert(event_id, pts=None, duration=None):
    """
    mk_cue returns a Cue
    with a Splice Insert.

    splice_event_id = event_id

    if pts is none:
        splice_immediate_flag      True
        time_specified_flag        False

    if pts:
        splice_immediate_flag      False
        time_specified_flag        True
        pts_time                   pts
   
    If duration is NOT set,
        out_of_network_indicator   False
        duration_flag              False
        

    if duration IS set:
        out_of_network_indicator   True
        duration_flag              True
        break_auto_return          True
        break_duration             duration
        pts_time                   pts

    
    """
    cue = Cue()
    # default is a CUE-IN
    sin = SpliceInsert()
    sin.splice_event_id = event_id
    sin.splice_event_cancel_indicator = False
    sin.out_of_network_indicator = False
    sin.duration_flag = False
    sin.unique_program_id = event_id
    sin.avail_num = 0
    sin.avail_expected = 0
    sin.splice_immediate_flag = True
    sin.time_specified_flag = False
    sin.program_splice_flag = False

    # pts = None for Splice Immediate
    if pts is not None:
        sin.program_splice_flag = True
        sin.splice_immediate_flag = False
        sin.time_specified_flag = True
        sin.pts_time= float(pts)
    else:
        sin.component_count=0
    # If we have a duration, make a CUE-OUT
    if duration is not None:
        duration = float(duration)
        sin.break_duration = duration
        sin.break_auto_return = True
        sin.duration_flag = True
        sin.out_of_network_indicator = True
    cue.command = sin  # Add SpliceInsert to the SCTE35 cue
    cue.encode()
    return cue
