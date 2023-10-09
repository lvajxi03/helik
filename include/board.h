#ifndef __BOARD_H__
#define __BOARD_H__

class Board
{
 public:
  Board();
  virtual ~Board();
  virtual void activate() = 0;
  virtual void deactivate() = 0;
  virtual void on_paint() = 0;
  virtual void on_keyup() = 0;
  virtual void on_mouseup() = 0;
  virtual void on_timer() = 0;
  virtual void on_update() = 0;
};

#endif /* __BOARD_H__ */
