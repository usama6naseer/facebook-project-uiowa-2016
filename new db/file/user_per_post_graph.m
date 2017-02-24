clear all
[a, b, col] = xlsread('users_per_post.csv');
[a1, b1, col1] = xlsread('likes_per_post.csv');
s = size(col)
sizex = s(1);
sizey = s(2);
count = 0;

for i=2:sizex
% for i=2:4
    figure;
    hold on;
%     x rows
%     y columns
    arr = col(i,2:sizey);
    arr = cell2mat(arr);
    arr(isnan(arr)) = [];
    ns = size(arr);
    nsizex = ns(1);
    nsizey = ns(2);
    
    plot(arr,'b','LineWidth',2,'MarkerEdgeColor','b')
%     
    arr = col1(i,2:sizey);
    arr = cell2mat(arr);
    arr(isnan(arr)) = [];
    ns = size(arr);
    nsizex = ns(1);
    nsizey = ns(2);
    plot(arr,'r','LineWidth',2,'MarkerEdgeColor','r')
    
    axis([1 nsizey 0 max(arr)*1.3])
    pageid = cell2mat(col(i,1));
    xlabel('Posts');
    ylabel('Number of Likes');
    t = strcat('Number of likes on page ID: ', pageid);
    title(t);
    
%     ax = gca;
%     set(ax,'XLim',[1 sizey-1])
%     set(ax,'XTick',[1:1:sizey-1])
%     set(ax,'XTickLabel',col(1,2:sizey))
%     ax.XTickLabelRotation = 45;
%     xticklabel_rotate([], 45, col(1,2:sizey))
    count = count + 1;
    print(num2str(count),'-dpng')
end



