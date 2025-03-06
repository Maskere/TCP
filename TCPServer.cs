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

                while(isRunning){
                    string? message = reader.ReadLine();

                    switch(message){
                        default:
                            writer.Write(message);
                            break;
                        case "Random":
                            Random random = new();
                            writer.Write("Input numbers");

                            string? toRandom = reader.ReadLine();
                            string[]? splitToRandom = toRandom?.Split();

                            if(int.TryParse(splitToRandom?[0], out int first)){
                                if(int.TryParse(splitToRandom?[1].Trim(), out int second)){
                                    if(first < second){
                                        writer.Write(random.Next(first, second + 1));
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
                            break;
                        case "Add":
                            writer.Write("Input numbers");

                            string? toAdd = reader.ReadLine();
                            string[]? splitToAdd = toAdd?.Split();
                            break;
                        case "Subtract":
                            writer.Write("Input numbers");

                            string? toSubtract = reader.ReadLine();
                            string[]? splitToSubtract = toSubtract?.Split();
                            break;
                    }
                }
            }
        }
    }
}
