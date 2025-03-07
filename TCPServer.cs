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

                    if(splitMessage?[0] == "Random" ||
                            splitMessage?[0] == "Add" ||
                            splitMessage?[0] == "Subtract"){
                        HandleIncomingMessage(writer,splitMessage, random);
                    }
                    else{
                        writer.Write(message);
                    }
                }
            }
        }

        static void HandleIncomingMessage(StreamWriter writer, string[]? splitMessage, Random random){
            if(int.TryParse(splitMessage?[1], out int firstResult)){
                if(int.TryParse(splitMessage?[2].Trim(), out int secondResult)){
                    if(splitMessage[0] == "Random"){
                        writer.Write(random.Next(firstResult, secondResult + 1));
                    }
                    else if(splitMessage[0] == "Add"){
                        writer.Write(firstResult + secondResult);
                    }
                    else if(splitMessage[0] == "Subtract"){
                        writer.Write(firstResult - secondResult);
                    }
                }
            }
        }
    }
}
