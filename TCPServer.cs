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
                    string[]? splitMessage = message?.Split();

                    switch(splitMessage?[0].Trim()){
                        case "Random":
                            Random(writer,splitMessage,random);
                            break;
                        case "Add":
                            Add(writer,splitMessage);
                            break;
                        case "Subtract":
                            Subtract(writer,splitMessage);
                            break;
                        default:
                            writer.Write(message);
                            break;
                    }
                }
            }
        }

        static void Random(StreamWriter writer,string[] splitMessage, Random random){
            if(int.TryParse(splitMessage?[1].ToString(), out int firstResult)){
                if(int.TryParse(splitMessage?[2].ToString(), out int secondResult)){
                    writer.Write(random.Next(firstResult, secondResult + 1));
                }
            }
        }

        static void Add(StreamWriter writer, string[] splitMessage){
            if(int.TryParse(splitMessage?[1], out int firstAdd)){
                if(int.TryParse(splitMessage?[2].Trim(), out int secondAdd)){
                    writer.Write(firstAdd + secondAdd);
                }
            }
        }

        static void Subtract(StreamWriter writer, string[] splitMessage){
            if(int.TryParse(splitMessage?[1], out int firstSubtract)){
                if(int.TryParse(splitMessage?[2].Trim(), out int secondSubtract)){
                    writer.Write(firstSubtract - secondSubtract);
                }
            }
        }
    }
}
