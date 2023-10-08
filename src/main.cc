#include "app.h"

int main(int argc, char **argv)
{
  Application *app = new Application();
  app->run();
  delete app;
}
