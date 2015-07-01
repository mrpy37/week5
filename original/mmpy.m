% �t�@�C���̃f�[�^��ǂݍ���
M = csvread('input_1.csv')
[n1,n2] = size(M);

% x���Wy���W���ꂼ��z��Ɋi�[
cityX = M(:,1)
cityY = M(:,2)

% �S�Ă̒��̋������v�Z����
for i = 1:n1
    for j = 1:n1
    D(i,j) = sqrt((cityX(i)-cityX(j))^2 +(cityY(i)-cityY(j))^2);
    end
end

% �����C�ǂ̒����Ȃ��ł��邩�C���i�[���邽�߂̔z��Data�𐶐�
n = n1*(n1-1)/2;
Data = zeros(n,3);

% ���ꂼ��̒����q�����Ă���񐔂��i�[���邽�߂̔z��table�𐶐�
table = zeros(n1,2);
table(1:n1) =  [1:n1];
k=1;

%�����C�n�_�C�I�_�̒��̏���ێ�
for i=1:n1
    for j=n1:-1:1  
        if D(i,j)==0
            break
        else
            Data(k,1)=D(i,j);
            Data(k,2)=i;
            Data(k,3)=j;
            k=k+1;
        end
    end
end

%�������\�[�g���C�����s�̂��̂��ꏏ�ɕ��ёւ�
Data=sortrows(Data);

%1�ԒZ��������ۑ�
Dis = Data(1,1);

%���̏���int�^�ɕϊ��C���̒����g�����񐔂��ۑ�
cityA = int8(Data(1,2));
start = cityA;
table(cityA,2) = table(cityA,2)+1;

cityB = int8(Data(1,3));
goal = cityB;
table(cityB,2) = table(cityB,2)+1;

j = 0;

%���������ɕێ����Ă�������
for i = 2:n
    %����|�C���^p�ɍ��݂Ă��钬�̔ԍ���ۑ�
    p1 = int8(Data(i,2));
    p2 = int8(Data(i,3));
    
    %�������̒������ł�2��g���Ă����烋�[�v�𔲂���
    if table(p1,2) == 2
       continue
    end
    if table(p2,2) == 2
        continue
    end
    if (table(p1,2) == 1) && (table(p2,2) == 1)
        continue
    end
    
        table(p1,2) = table(p1,2)+1;
        table(p2,2) = table(p2,2)+1;
        Dis = Dis + Data(i,1);
        j = j+1;
        
        if j == int8(n1/2)
            break
        end
end

for i = 1:n1
    if table(i,2) == 2
        break
    end
end
%�����܂ł�OK

%{
for j = 2:n
    %����|�C���^p�ɍ��݂Ă��钬�̔ԍ���ۑ�
    p1 = int8(Data(j,2));
    p2 = int8(Data(j,3));
    
    %�������̒������ł�2��g���Ă����烋�[�v�𔲂���
    if p1 == i
       continue
    end
    if p2 == i
        continue
    end
    
    for k = j+1:n
        p3 = int8(Data(k,2));
        p4 = int8(Data(k,3));
        
        if p3 == p1 
            continue
        end
        
        if p3 == p2 
            continue
        end
        
        if p4 == p1 
            continue
        end
        
        if p4 == p2 
            continue
        end
        
  %}      