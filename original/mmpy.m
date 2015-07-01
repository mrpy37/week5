% ファイルのデータを読み込む
M = csvread('input_1.csv')
[n1,n2] = size(M);

% x座標y座標それぞれ配列に格納
cityX = M(:,1)
cityY = M(:,2)

% 全ての町の距離を計算する
for i = 1:n1
    for j = 1:n1
    D(i,j) = sqrt((cityX(i)-cityX(j))^2 +(cityY(i)-cityY(j))^2);
    end
end

% 距離，どの町をつないでいるか，を格納するための配列Dataを生成
n = n1*(n1-1)/2;
Data = zeros(n,3);

% それぞれの町が繋げられている回数を格納するための配列tableを生成
table = zeros(n1,2);
table(1:n1) =  [1:n1];
k=1;

%距離，始点，終点の町の情報を保持
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

%距離をソートし，同じ行のものも一緒に並び替え
Data=sortrows(Data);

%1番短い距離を保存
Dis = Data(1,1);

%町の情報をint型に変換，その町を使った回数も保存
cityA = int8(Data(1,2));
start = cityA;
table(cityA,2) = table(cityA,2)+1;

cityB = int8(Data(1,3));
goal = cityB;
table(cityB,2) = table(cityB,2)+1;

j = 0;

%小さい順に保持していく処理
for i = 2:n
    %あるポインタpに今みている町の番号を保存
    p1 = int8(Data(i,2));
    p2 = int8(Data(i,3));
    
    %もしその町がすでに2回使われていたらループを抜ける
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
%ここまではOK

%{
for j = 2:n
    %あるポインタpに今みている町の番号を保存
    p1 = int8(Data(j,2));
    p2 = int8(Data(j,3));
    
    %もしその町がすでに2回使われていたらループを抜ける
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