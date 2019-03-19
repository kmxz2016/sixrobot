# This Python file uses the following encoding: utf-8
"""autogenerated by genpy from sixrobot_core_msgs/RobustControllerStatus.msg. Do not edit."""
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct


class RobustControllerStatus(genpy.Message):
  _md5sum = "2f15441b7285d915e7e59d3618e173f2"
  _type = "sixrobot_core_msgs/RobustControllerStatus"
  _has_header = False #flag to mark the presence of a Header object
  _full_text = """# True if the RC is enabled and running, false if not.
bool isEnabled

# The state of the RC with respect to its completion goal.  One of
# NOT_COMPLETE, COMPLETE_W_FAILURE, or COMPLETE_W_SUCCESS
int32 complete
int32 NOT_COMPLETE = 0
int32 COMPLETE_W_FAILURE = 1
int32 COMPLETE_W_SUCCESS = 2

# Identifies the sender of the Enable message that the RC is using for its
# commands.  This should correspond to the "uid" field of a recently published
# RC *Enable message.
string controlUid

# Set to true when the RC self-disables as a result of too much time elapsing
# without receiving an Enable message.
bool timedOut

# A list of relevant error codes.  Error codes are defined by the individual
# robust controllers, consult a robust controller's documentation to see what
# error codes it generates.
string[] errorCodes

# A list of current labels for the RC's current state. For example, "fastapproach",
# "slowapproach", etc. Used primarily for the blended RCs, other RCs can leave this
# blank. This will probably contains just one label, but it could contain multiple labels
# in the future.
string[] labels
"""
  # Pseudo-constants
  NOT_COMPLETE = 0
  COMPLETE_W_FAILURE = 1
  COMPLETE_W_SUCCESS = 2

  __slots__ = ['isEnabled','complete','controlUid','timedOut','errorCodes','labels']
  _slot_types = ['bool','int32','string','bool','string[]','string[]']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       isEnabled,complete,controlUid,timedOut,errorCodes,labels

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(RobustControllerStatus, self).__init__(*args, **kwds)
      #message fields cannot be None, assign default values for those that are
      if self.isEnabled is None:
        self.isEnabled = False
      if self.complete is None:
        self.complete = 0
      if self.controlUid is None:
        self.controlUid = ''
      if self.timedOut is None:
        self.timedOut = False
      if self.errorCodes is None:
        self.errorCodes = []
      if self.labels is None:
        self.labels = []
    else:
      self.isEnabled = False
      self.complete = 0
      self.controlUid = ''
      self.timedOut = False
      self.errorCodes = []
      self.labels = []

  def _get_types(self):
    """
    internal API method
    """
    return self._slot_types

  def serialize(self, buff):
    """
    serialize message into buffer
    :param buff: buffer, ``StringIO``
    """
    try:
      _x = self
      buff.write(_get_struct_Bi().pack(_x.isEnabled, _x.complete))
      _x = self.controlUid
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.pack('<I%ss'%length, length, _x))
      buff.write(_get_struct_B().pack(self.timedOut))
      length = len(self.errorCodes)
      buff.write(_struct_I.pack(length))
      for val1 in self.errorCodes:
        length = len(val1)
        if python3 or type(val1) == unicode:
          val1 = val1.encode('utf-8')
          length = len(val1)
        buff.write(struct.pack('<I%ss'%length, length, val1))
      length = len(self.labels)
      buff.write(_struct_I.pack(length))
      for val1 in self.labels:
        length = len(val1)
        if python3 or type(val1) == unicode:
          val1 = val1.encode('utf-8')
          length = len(val1)
        buff.write(struct.pack('<I%ss'%length, length, val1))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize(self, str):
    """
    unpack serialized message in str into this message instance
    :param str: byte array of serialized message, ``str``
    """
    try:
      end = 0
      _x = self
      start = end
      end += 5
      (_x.isEnabled, _x.complete,) = _get_struct_Bi().unpack(str[start:end])
      self.isEnabled = bool(self.isEnabled)
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.controlUid = str[start:end].decode('utf-8')
      else:
        self.controlUid = str[start:end]
      start = end
      end += 1
      (self.timedOut,) = _get_struct_B().unpack(str[start:end])
      self.timedOut = bool(self.timedOut)
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      self.errorCodes = []
      for i in range(0, length):
        start = end
        end += 4
        (length,) = _struct_I.unpack(str[start:end])
        start = end
        end += length
        if python3:
          val1 = str[start:end].decode('utf-8')
        else:
          val1 = str[start:end]
        self.errorCodes.append(val1)
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      self.labels = []
      for i in range(0, length):
        start = end
        end += 4
        (length,) = _struct_I.unpack(str[start:end])
        start = end
        end += length
        if python3:
          val1 = str[start:end].decode('utf-8')
        else:
          val1 = str[start:end]
        self.labels.append(val1)
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e) #most likely buffer underfill


  def serialize_numpy(self, buff, numpy):
    """
    serialize message with numpy array types into buffer
    :param buff: buffer, ``StringIO``
    :param numpy: numpy python module
    """
    try:
      _x = self
      buff.write(_get_struct_Bi().pack(_x.isEnabled, _x.complete))
      _x = self.controlUid
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.pack('<I%ss'%length, length, _x))
      buff.write(_get_struct_B().pack(self.timedOut))
      length = len(self.errorCodes)
      buff.write(_struct_I.pack(length))
      for val1 in self.errorCodes:
        length = len(val1)
        if python3 or type(val1) == unicode:
          val1 = val1.encode('utf-8')
          length = len(val1)
        buff.write(struct.pack('<I%ss'%length, length, val1))
      length = len(self.labels)
      buff.write(_struct_I.pack(length))
      for val1 in self.labels:
        length = len(val1)
        if python3 or type(val1) == unicode:
          val1 = val1.encode('utf-8')
          length = len(val1)
        buff.write(struct.pack('<I%ss'%length, length, val1))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize_numpy(self, str, numpy):
    """
    unpack serialized message in str into this message instance using numpy for array types
    :param str: byte array of serialized message, ``str``
    :param numpy: numpy python module
    """
    try:
      end = 0
      _x = self
      start = end
      end += 5
      (_x.isEnabled, _x.complete,) = _get_struct_Bi().unpack(str[start:end])
      self.isEnabled = bool(self.isEnabled)
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.controlUid = str[start:end].decode('utf-8')
      else:
        self.controlUid = str[start:end]
      start = end
      end += 1
      (self.timedOut,) = _get_struct_B().unpack(str[start:end])
      self.timedOut = bool(self.timedOut)
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      self.errorCodes = []
      for i in range(0, length):
        start = end
        end += 4
        (length,) = _struct_I.unpack(str[start:end])
        start = end
        end += length
        if python3:
          val1 = str[start:end].decode('utf-8')
        else:
          val1 = str[start:end]
        self.errorCodes.append(val1)
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      self.labels = []
      for i in range(0, length):
        start = end
        end += 4
        (length,) = _struct_I.unpack(str[start:end])
        start = end
        end += length
        if python3:
          val1 = str[start:end].decode('utf-8')
        else:
          val1 = str[start:end]
        self.labels.append(val1)
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e) #most likely buffer underfill

_struct_I = genpy.struct_I
def _get_struct_I():
    global _struct_I
    return _struct_I
_struct_B = None
def _get_struct_B():
    global _struct_B
    if _struct_B is None:
        _struct_B = struct.Struct("<B")
    return _struct_B
_struct_Bi = None
def _get_struct_Bi():
    global _struct_Bi
    if _struct_Bi is None:
        _struct_Bi = struct.Struct("<Bi")
    return _struct_Bi
