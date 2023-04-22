#include <iostream>
#include <string>

void parse_key(const std::string& key) 
{
  std::cout << "Key: " << key << std::endl;
}

int main(int argc, char **argv) {

  if (!(std::string(argv[1]).compare("-g")))
  {
    std::cout << "Falg -g" << std::endl;
    if (argc < 2) {
      std::cout << "Usage: " << argv[0] << " <flag> [<key>]" << std::endl;
      exit(1);
    }
    else
      parse_key(std::string(argv[2]));
  }
  else if (!(std::string(argv[1]).compare("-k"))) std::cout << "Falg -k"
                                                            << std::endl;
  else {
    std::cout << "[!] Incorrect Flag" << std::endl;
    exit(1);
  }
}
