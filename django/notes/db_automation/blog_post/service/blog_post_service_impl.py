from account.repository.account_repository_impl import AccountRepositoryImpl
from account_profile.repository.account_profile_repository_impl import AccountProfileRepositoryImpl
from blog_post.entity.blog_post import BlogPost
from blog_post.repository.blog_post_repository_impl import BlogPostRepositoryImpl
from blog_post.service.blog_post_service import BlogPostService


class BlogPostServiceImpl(BlogPostService):
    __instance = None

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)

            cls.__instance.__blogPostRepository = BlogPostRepositoryImpl.getInstance()
            cls.__instance.__accountRepository = AccountRepositoryImpl.getInstance()
            cls.__instance.__accountProfileRepository = AccountProfileRepositoryImpl.getInstance()

        return cls.__instance

    @classmethod
    def getInstance(cls):
        if cls.__instance is None:
            cls.__instance = cls()

        return cls.__instance

    def requestCreate(self, title, content, accountId):
        if not title or not content:
            raise ValueError("Title and content are required fields.")
        if not accountId:
            raise ValueError("Account ID is required.")

            # 2. Account 조회
        account = self.__accountRepository.findById(accountId)
        if not account:
            raise ValueError(f"Account with ID {accountId} does not exist.")

        # 3. AccountProfile 조회
        accountProfile = self.__accountProfileRepository.findByAccount(account)
        if not accountProfile:
            raise ValueError(f"AccountProfile for account ID {accountId} does not exist.")

        # 4. Board 객체 생성 및 저장
        blogPost = BlogPost(
            title=title,
            content=content,
            writer=accountProfile)  # ForeignKey로 연결된 account_profile)
        savedBlogPost = self.__blogPostRepository.save(blogPost)

        # 5. 응답 데이터 구조화
        return {
            "boardId": savedBlogPost.id,
            "title": savedBlogPost.title,
            "writerNickname": savedBlogPost.writer.nickname,
            "createDate": savedBlogPost.create_date.strftime("%Y-%m-%d %H:%M"),
        }