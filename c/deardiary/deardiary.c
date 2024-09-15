#include <stdio.h>
#include <conio.h>
#include <string.h>

int signup();
int login();
int book(const char *refer);
int append(const char *apd);
int write(const char *wrt);
int read(const char *red);
int display();

int userCount = 0;
struct data {
    char user_name[25];
    char password[20];
    char e_mail[20];
} user[100];

int fileExists(const char *filename) {
    FILE *file = fopen(filename, "r");
    if (file) {
        fclose(file);
        return 1;
    }
    return 0;
}

int main() {
    int n, i;
    char *token;
    char *line, part[100];
    FILE *file;

    if (!fileExists("userData.csv")) {
        printf("File 'userData.csv' does not exist. Creating...\n");
        file = fopen("userData.csv", "w");
        if (file == NULL) {
            printf("Error creating file 'userData.csv'\n");
            getch();
            goto end;
        }
        fclose(file);
        printf("File 'userData.csv' created successfully.\n press any key to continue");
        getch();
    }



    file = fopen("userData.csv", "r");
    if (file == NULL) {
        printf("Error opening file 'userData.csv'\n");
        getch();
        goto end;
    }

    while (fgets(part, sizeof(part), file)) {
        line = strtok(part, "\n");
        token = strtok(line, ",");
        strcpy(user[userCount].user_name, token);
        token = strtok(NULL, " ");
        strcpy(user[userCount].password, token);
        userCount++;
    }
    fclose(file);

front:
    clrscr();
    printf("======================== DEAR === DIARY ========================\n\n");
    printf("press 1 for signup\tpress 2 for login\tpress 0 for exit\n==> ");
    scanf("%d", &n);

    switch (n) {
    default:
        goto front;
        break;
    case 1:
        signup();
        goto front;
        break;
    case 2:
        login();
        goto front;
        break;
    case 693:
        display();
        goto front;
        break;
    case 0:
        printf("exiting...");
        break;
    }
    getch();
end:
    return 0;
}

int signup() {
    int i;
    char CheckName[25];
    FILE *file;
    UN:
    clrscr();
        printf("======================== DEAR === DIARY ========================\n\n");
    printf("Enter your e-mail: ");
    scanf("%s", user[userCount].e_mail);
    if (strstr(user[userCount].e_mail, "@gmail.com") == NULL) {
        printf("Invalid email! Add '@gmail.com'.\n");
        getch();
        goto UN;
    }

    printf("Enter your user name: ");
    scanf("%s", CheckName);

    for (i = 0; i < userCount; i++) {
        if (strcmp(CheckName, user[i].user_name) == 0) {
            printf("Username already exists! Please choose a different one.\n");
            getch();
            goto UN;
        }
    }
    printf("Enter your password: ");
    scanf("%s", user[userCount].password);

    strcpy(user[userCount].user_name, CheckName);
    userCount++;

    file = fopen("userData.csv", "a");
    if (file == NULL) {
        printf("Error opening file\n");
        return 1;
    }
    fprintf(file, "%s,%s \n", CheckName, user[userCount - 1].password);
    fclose(file);

    return 0;
}

int login() {
    int i, n;
    char name[25], passkey[20], refer[30];
    printf("Enter user name: ");
    scanf("%s", name);
    printf("Enter your password: ");
    scanf("%s", passkey);
    clrscr();
    printf("======================== DEAR === DIARY ========================\n\n");
    for(i = 0; i < userCount; i++) {
        if(strcmp(name, user[i].user_name) == 0 && strcmp(passkey, user[i].password) == 0) {

            printf("Login successful!\n\n");
            printf("Hello %s\n\n",name);
            strcpy(refer, name);
            strcat(refer, ".txt");
            book(refer);
            return 0;
        }
    }

    printf("Invalid username or password. Do you want to create a new account?\n");
    printf("1. Yes\t2. No\n==> ");
    scanf("%d", &n);
    switch(n) {
        case 1:
            signup();
            return 0;
        case 2:
            break;
    }

    return 0;
}



int book(const char *refer){
    int choice;
    char copy[30];
    strcpy(copy,refer);
    books:
    printf("\n\npress 1 for reading the diary \tpress 2 for writing \n\npress 3 for continue writing\tpress any key to exit\n==> ");
    scanf("%d",&choice);
    switch(choice){
    case 1:
        read(copy);
        goto books;
        break;
    case 2:
        write(copy);
        goto books;
        break;
    case 3:
        append(copy);
        goto books;
        break;
    default:
        break;
    }
    return 0;
}

int append(const char *apd){
    char reader;
    FILE *userFile = fopen(apd,"a");

    if(userFile == NULL) {
        printf("Error opening file for user\n");
        return 1;
    }

    printf("Dear Diary: ");
    while((reader=getchar())!=EOF)
    {
        putc(reader,userFile);
    }
    fclose(userFile);
    return 0;
}

int read(const char *red){
    char reader;
    FILE *userFile = fopen(red,"r");

    if(userFile == NULL) {
        printf("Error opening file for user\n");
        getch();
        return 1;
    }

    printf("reading dear diary:");
    while((reader=getc(userFile))!=EOF){
        printf("%c",reader);
    }
    fclose(userFile);
    getch();
    return 0;
}

int write(const char *wrt){
    char reader;
    FILE *userFile;
    userFile = fopen(wrt,"w");

    if(userFile == NULL) {
        printf("Error creating file for user\n");
        return 1;
    }

    printf("Dear Diary Created\n");
    while((reader=getchar())!=EOF)
    {
        putc(reader,userFile);
    }
    fclose(userFile);
    return 0;
}

int display()
{
    int count=1;
    char *line,part[100];
    char *token;
    FILE *file = fopen("userData.csv","r");
    if (file == NULL) {
        printf("Error opning file \n");
        getch();
        return 0;
    }

    while (fgets(part, sizeof(part), file)) {
        line = strtok(part,"\n");
        token = strtok(line, ",");
        printf("User no  :%d\t",count);
        strcpy(user[userCount].user_name, token);
        printf("Username :%s\t",user[userCount].user_name);
        token = strtok(NULL, " ");
        strcpy(user[userCount].password, token);
        printf("Password :%s\n",user[userCount].password);
        count++;
    }
    fclose(file);
    getch();
    return 0;
}

