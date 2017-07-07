import numpy as np

def sample(probs):
  return np.random.choice(len(probs), None, p=probs)

class MonitorCallable():

  def __init__(self, video_ep_freq=100):
    self.video_ep_freq = video_ep_freq

  def call(self, idx):
    if self.video_ep_freq == 0:
      return False
    else:
      return (idx != 0) and (idx % self.video_ep_freq == 0)

class Timer(object):

  def __init__(self):
    self.times = {}
    self.counts = {}

  def add(self, name, value):

    if name in self.times:
      self.times[name] += value
      self.counts[name] += 1
    else:
      self.times[name] = value
      self.counts[name] = 1

  def reset(self, name):
    self.times[name] = 0
    self.counts[name] = 0

  def reset_all(self):
    for key in self.times.keys():
      self.times[key] = 0
      self.counts[key] = 0

  def print(self):
    for key in self.times.keys():
      print("%s: %.8f" % (key, (self.times[key] / self.counts[key])))