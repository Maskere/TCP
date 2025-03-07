using System.Net.Sockets;

namespace TCP{
    public class TCPServer{
        public static void HandleClient(TcpClient socket, int port){
            bool isRunning = true;

            using(socket){
                NetworkStream ns = socket.GetStream();

                StreamReader reader = new(ns);
                StreamWriter writer = new(ns);
                writer.AutoFlush = true;

                Random random = new();
                while(isRunning){
                    string? message = reader.ReadLine();

                    switch(message){
                        default:
                            writer.Write(message);
                            break;
                        case "Random":
                            Random(writer,reader,random);
                            break;
                        case "Add":
                            Add(writer,reader);
                            break;
                        case "Subtract":
                            Subtract(writer,reader);
                            break;
                    }
                }
            }
        }

        static void Random(StreamWriter writer, StreamReader reader,Random random){
            writer.Write("Input numbers");

            string? toRandom = reader.ReadLine();
            string[]? splitToRandom = toRandom?.Split();

            if(int.TryParse(splitToRandom?[0], out int firstRandom)){
                if(int.TryParse(splitToRandom?[1].Trim(), out int secondRandom)){
                    if(firstRandom < secondRandom){
                        writer.Write(random.Next(firstRandom, secondRandom + 1));
                    }
                    else{
                        writer.Write("First number must be higher than the second number");
                    }
                }
                else{
                    writer.Write("Invalid input");
                }
            }
            else{
                writer.Write("Invalid input");
            }
        }

        static void Add(StreamWriter writer, StreamReader reader){
            writer.Write("Input numbers");

            string? toAdd = reader.ReadLine();
            string[]? splitToAdd = toAdd?.Split();

            if(int.TryParse(splitToAdd?[0], out int firstAdd)){
                if(int.TryParse(splitToAdd?[1].Trim(), out int secondAdd)){
                    writer.Write(firstAdd + secondAdd);
                }
                else{
                    writer.Write("Invalid input");
                }
            }
            else{
                writer.Write("Invalid input");
            }
        }

        static void Subtract(StreamWriter writer, StreamReader reader){
            writer.Write("Input numbers");

            string? toSubtract = reader.ReadLine();
            string[]? splitToSubtract = toSubtract?.Split();

            if(int.TryParse(splitToSubtract?[0], out int firstSubtract)){
                if(int.TryParse(splitToSubtract?[1].Trim(), out int secondSubtract)){
                    writer.Write(firstSubtract - secondSubtract);
                }
                else{
                    writer.Write("Invalid input");
                }
            }
            else{
                writer.Write("Invalid input");
            }
        }
    }
}
