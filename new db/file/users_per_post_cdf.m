clear all
[a, b, col] = xlsread('users_per_post.csv');
s = size(col)
sizex = s(1);
sizey = s(2);
count = 0;

for i=2:sizex
    figure;
%     x rows
%     y columns
    arr = col(i,2:sizey);
    arr = cell2mat(arr);
    arr(isnan(arr)) = [];
    ns = size(arr);
    nsizex = ns(1);
    nsizey = ns(2);
    
    new_arr = zeros(1,nsizey);
    pre = 0;
    for ind = 1:nsizey
        new_arr(ind) = pre + arr(ind);
        if ind > 1
            pre = new_arr(ind);
        end
    end
    
    plot(new_arr,'LineWidth',2)
    axis([1 nsizey 0 max(new_arr)*1.3])
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



