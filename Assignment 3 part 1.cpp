#include <iostream>
using namespace std;
int main() {
    cout << "Subnet: \nA subnet (subnetwork) is a smaller network created by dividing a larger network into multiple smaller networks.\n";
    cout<<"Subnet Mask:\nA subnet mask is a 32-bit number used with an IPv4 address to divide it into two parts:\n1. Network ID – identifies the network.\n2. Host ID – identifies the device (host) on that network.\n";
    string ip;
    cout << "\nEnter IP Address: ";
    cin >> ip;

    // Extract first octet
    int firstOctet = 0;
    int i = 0;

    while (ip[i] != '.') {
        firstOctet = firstOctet * 10 + (ip[i] - '0');
        i++;
    }

    cout << "\nIP Address: " << ip << endl;

    if (firstOctet >= 1 && firstOctet <= 126) {
        cout << "Class: A" << endl;
        cout << "Default Subnet Mask: 255.0.0.0" << endl;
        cout << "Number of Networks: 2^7" << endl;
        cout << "Reason: First bit is fixed as 0, leaving 7 bits for network IDs.\n";
        cout << "        2^7 = 128 possible networks.\n";
        cout << "        Subtract 2 (Network 0 and 127 reserved).\n\n";
        cout << "Number of Hosts per Network: 2^24 - 2" << endl;
        cout << "Reason: 24 host bits are available.\n";
        cout << "        Subtract 2 (Network Address and Broadcast Address)." << endl;
    }
    else if (firstOctet >= 128 && firstOctet <= 191) {
        cout << "Class: B" << endl;
        cout << "Default Subnet Mask: 255.255.0.0" << endl;
        cout << "Number of Networks: 2^14" << endl;
        cout << "Reason: First two bits are fixed as 10, leaving 14 bits for network IDs.\n\n";
        cout << "Number of Hosts per Network: 2^16 - 2" << endl;
         cout << "Reason: 16 host bits are available.\n";
        cout << "        Subtract 2 (Network Address and Broadcast Address)." << endl;
    }
    else if (firstOctet >= 192 && firstOctet <= 223) {
        cout << "Class: C" << endl;
        cout << "Default Subnet Mask: 255.255.255.0" << endl;
        cout << "Number of Networks: 2^21" << endl;
         cout << "Reason: First three bits are fixed as 110, leaving 21 bits for network IDs.\n\n";
        cout << "Number of Hosts per Network: 2^8 - 2" << endl;
        cout << "Reason: 8 host bits are available.\n";
        cout << "        Subtract 2 (Network Address and Broadcast Address)." << endl;
    }
    else if (firstOctet >= 224 && firstOctet <= 239) {
        cout << "Class: D" << endl;
        cout << "Used for Multicasting" << endl;
    }
    else if (firstOctet >= 240 && firstOctet <= 255) {
        cout << "Class: E" << endl;
        cout << "Reserved for Experimental Use" << endl;
    }
    else {
        cout << "Invalid IP Address!" << endl;
    }
   
    //loopback
    cout<<"Loopback Address: \nA loopback address is a special IP address used by a computer to communicate with itself. The IPv4 loopback address is 127.0.0.1,\n Purpose: \nIt is mainly used for testing the TCP/IP stack, network applications, and troubleshooting network issues. Packets sent to a loopback address never leave the local machine.";
   

    return 0;
}
