#include <iostream>
#include <string>
#include <curl/curl.h>
#include <nlohmann/json.hpp>

static size_t WriteCallback(void *contents, size_t size, size_t nmemb, void *userp){
    ((std::string*)userp)->append((char*)contents, size * nmemb);
    return size * nmemb;
}

void setAllZeros(char arr[], int size){
    for(int i = 0; i < size; i++){
        arr[i] = '_';
    }
}

void hangman(std::string secret, int count){
    std::cout << "Ditt ord består av " << count << " bokstaver." << std::endl;
    int points = 0;

    char guessed[count];
    setAllZeros(guessed, count);

    while(true){
        std::cout << "Gjett en bokstav: ";
        char c; std::cin >> c;

        for(int i = 0; i < count; i++){
            if(secret[i] == c){
                guessed[i] = c; 
                points++;
            }
        }
        std::cout << guessed << std::endl;
        if(points == count){
            std::cout << "Du vant!\n"; 
            break;
        }
    }
}

int main(void){
    CURL *curl;
    CURLcode res;
    std::string readBuffer;
    std::string secretWord;
    int wordCount;

    curl = curl_easy_init();
    if(curl) {
        // Lese content inn til readBuffer
        curl_easy_setopt(curl, CURLOPT_URL, "https://api.kodesonen.no/?task=hangman");
        curl_easy_setopt(curl, CURLOPT_WRITEFUNCTION, WriteCallback);
        curl_easy_setopt(curl, CURLOPT_WRITEDATA, &readBuffer);
        res = curl_easy_perform(curl);
        curl_easy_cleanup(curl);

        // Gjør om string readBuffer til json objekt
        nlohmann::json json_object = nlohmann::json::parse(readBuffer);
    
        // Parse ut alle strings
        auto json_parse = json_object.get<std::unordered_map<std::string, nlohmann::json>>();

        // Sjekk om left-side string er random-word. Isåfall hent ut right-side.
        for (auto i : json_parse){
            if(i.first == "random-word") secretWord = i.second;
            if(i.first == "characters") wordCount = i.second;
        }
        
        hangman(secretWord, wordCount);
    }
    return 0;
}
